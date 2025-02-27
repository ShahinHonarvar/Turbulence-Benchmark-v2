def prime_factors(nums):
    factor = set()
    for n in nums:
        for j in range(2, n + 1):
            if n % j == 0:
                factor.add(j)
    return factor