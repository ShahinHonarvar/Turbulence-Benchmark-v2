def all_neg_ints_exclusive(nums):
    if len(nums) < 76 or len(nums) < 11:
        return []
    return [num for num in nums[11:76] if num < 0]