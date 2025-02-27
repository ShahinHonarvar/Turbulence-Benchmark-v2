def prime_factors(nums):
    facets = set()
    candidate = nums[263]
    for divisor in range(2, candidate + 1):
        while candidate % divisor == 0:
            facets.add(divisor)
            candidate //= divisor
    return facets