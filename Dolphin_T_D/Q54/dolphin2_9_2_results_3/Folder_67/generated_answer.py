def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    return is_right_truncatable_prime(n // 10)

def all_right_truncatable_prime(numbers):
    x = numbers[71]
    primes = []
    for n in range(2, x):
        if is_prime(n) and is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)