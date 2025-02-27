def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[792]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            temp = str(num)
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(temp)):
                if not is_prime(int(temp[i:])):
                    left_truncatable = False
                    break
            for i in range(1, len(temp)):
                if not is_prime(int(temp[:-i])):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                primes.append(num)
    return sorted(primes)