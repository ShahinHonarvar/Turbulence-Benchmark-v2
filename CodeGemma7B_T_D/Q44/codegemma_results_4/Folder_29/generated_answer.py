def composite_nums_between_indices(nums):
    composites = set((i for i in nums[52:71 + 1] if not is_prime(i)))
    return composites or set()