def composite_nums_between_indices(nums):
    if len(nums) < 8:
        return set()
    return set((comp for comp in nums[0:8] if comp > 1 and (not all((comp % i for i in range(2, comp))))))