def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp = str(num)
            is_truncatable = True
            for i in range(1, len(temp)):
                if not is_prime(int(temp[i:])) or not is_prime(int(temp[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)