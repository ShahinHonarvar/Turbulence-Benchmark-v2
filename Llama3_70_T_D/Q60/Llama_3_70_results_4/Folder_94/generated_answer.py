def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    primes = []
    for num in range(10, x + 1):
        if '0' not in str(num):
            left_truncatable = True
            right_truncatable = True
            temp = str(num)
            for _ in range(len(temp) - 1):
                if not is_prime(int(temp[:-1])):
                    left_truncatable = False
                    break
                temp = temp[:-1]
            temp = str(num)
            for _ in range(len(temp) - 1):
                if not is_prime(int(temp[1:])):
                    right_truncatable = False
                    break
                temp = temp[1:]
            if is_prime(num) and left_truncatable and right_truncatable:
                primes.append(num)
    return sorted(primes)