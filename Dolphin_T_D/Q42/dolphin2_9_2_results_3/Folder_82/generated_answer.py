def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    return set([i for i in range(2, numbers[83] + 1) if is_prime(i) and numbers[83] % i == 0])