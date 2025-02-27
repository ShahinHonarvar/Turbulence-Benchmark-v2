def prime_factors(nums):
    return factors(nums[13])

def factors(n):
    """
    Calculates the factors of a positive integer n.
    """
    factors = set()
    for x in range(2, n + 1):
        while n % x == 0:
            factors.add(x)
            n //= x
    return factors