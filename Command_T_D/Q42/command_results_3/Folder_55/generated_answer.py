def prime_factors(nums):
    return set((i for i in range(2, int(nums[21]) + 1) if all((nums[j] % i for j in range(21)))))