def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    return set((i for i in range(2, int(numbers[95] ** 0.5) + 1) if numbers[95] % i == 0 and is_prime(i)))