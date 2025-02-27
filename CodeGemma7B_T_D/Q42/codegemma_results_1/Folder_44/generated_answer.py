def prime_factors(nums):
    factors = set()
    for divisor in range(2, int(nums[828] ** 0.5) + 1):
        while nums[828] % divisor == 0:
            factors.add(divisor)
            nums[828] //= divisor
    if nums[828] > 1:
        factors.add(nums[828])
    return factors