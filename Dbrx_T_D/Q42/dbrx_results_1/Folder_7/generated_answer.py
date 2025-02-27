def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = numbers[851]
    factors = set()
    for potential_factor in range(2, num + 1):
        if num % potential_factor == 0 and is_prime(potential_factor):
            factors.add(potential_factor)
    return factors