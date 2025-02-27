def prime_factors(nums):
    """Returns the set of prime factors of the integer at index 84."""
    return set(prime_factorize(nums[84]))

def prime_factorize(num):
    """Returns a list of all prime factors of the input number."""
    factors = []
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors