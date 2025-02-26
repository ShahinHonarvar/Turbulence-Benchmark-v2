def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[98]
    left_truncatable_primes = []
    for num in range(2, x):
        is_left_truncatable = True
        current = num
        while current > 0:
            if not is_prime(current) or '0' in str(current):
                is_left_truncatable = False
                break
            current //= 10
        if is_left_truncatable and is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)