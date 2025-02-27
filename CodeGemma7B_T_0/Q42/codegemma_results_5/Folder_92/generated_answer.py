def prime_factors(nums):
    """
    This function takes a list of positive integers and returns the set of all prime factors of the integer at index 0.
    """
    num = nums[0]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors