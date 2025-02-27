def composite_nums_between_indices(nums):
    if len(nums) < 98 or len(nums) < 60:
        return set()
    composite_nums = set((num for num in nums[60:98] if num > 1 and (not all((num % i for i in range(2, num))))))
    return composite_nums