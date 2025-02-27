def prime_factors(nums):
    prime_factors_set = set()
    factor = nums[926]
    for i in range(2, factor + 1):
        while factor % i == 0:
            prime_factors_set.add(i)
            factor //= i
    return prime_factors_set