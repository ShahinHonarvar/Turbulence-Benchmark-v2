def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    return set((factor for number in numbers for factor in range(2, number + 1) if is_prime(factor) and number % factor == 0))

def get_prime_factors_at_index_80(numbers):
    prime_factors_at_80 = prime_factors(numbers)[80]
    return set((i for i in prime_factors_at_80 if is_prime(i)))