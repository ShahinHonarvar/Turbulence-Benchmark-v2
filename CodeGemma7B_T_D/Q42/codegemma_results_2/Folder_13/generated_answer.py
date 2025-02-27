def prime_factors(nums):
    prime_factors_set = set()
    num_to_factor = nums[126]
    for factor in range(2, num_to_factor):
        while num_to_factor % factor == 0:
            num_to_factor //= factor
            prime_factors_set.add(factor)
    return prime_factors_set