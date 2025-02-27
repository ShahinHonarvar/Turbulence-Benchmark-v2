def all_neg_ints_exclusive(nums):
    if len(nums) < 2:
        return []
    return [num for num in nums[0:2] if num < 0]