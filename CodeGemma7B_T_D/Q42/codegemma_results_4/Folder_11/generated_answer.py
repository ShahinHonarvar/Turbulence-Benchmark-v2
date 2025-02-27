def prime_factors(nums):
    return set((factor for number in nums for factor in get_prime_factors(number)))

def get_prime_factors(number):
    """Helper function to get the prime factors of a number."""
    factors = set()
    for divisor in range(2, int(number ** 0.5) + 1):
        while number % divisor == 0:
            factors.add(divisor)
            number //= divisor
    if number > 1:
        factors.add(number)
    return factors