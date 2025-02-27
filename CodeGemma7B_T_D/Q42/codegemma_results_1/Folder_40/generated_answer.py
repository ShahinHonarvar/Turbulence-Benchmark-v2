def prime_factors(nums):
    """Return prime factors of the number at index 7 in the list of positive integers."""
    return set(prime_factorize(nums[7]))

def prime_factorize(n):
    """Return the prime factors of the number n."""
    factors = set()
    if n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.add(i)
                n //= i
    if n > 1:
        factors.add(n)
    return factors