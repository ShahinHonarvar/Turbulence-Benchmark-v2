def prime_factors(nums):
    factor_set = set()
    index = 849
    if 0 <= index < len(nums):
        num = nums[index]
        for i in range(2, num + 1):
            while num % i == 0:
                factor_set.add(i)
                num //= i
    return factor_set