def composite_nums_between_indices(nums):
    return set((n for n in nums[4:6] if n >= 4 and (not (n < 4 and all((n % d for d in range(2, int(n ** 0.5) + 1)))))))