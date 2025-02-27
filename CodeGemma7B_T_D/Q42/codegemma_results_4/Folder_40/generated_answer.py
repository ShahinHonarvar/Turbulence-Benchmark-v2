def prime_factors(nums):
    factor_set = set()
    seventeen_factor = nums[7]
    for num in range(2, seventeen_factor):
        while seventeen_factor % num == 0:
            factor_set.add(num)
            seventeen_factor //= num
    return factor_set