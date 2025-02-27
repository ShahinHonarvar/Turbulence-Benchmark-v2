def all_neg_ints_inclusive(nums):
    if len(nums) < 52:
        return []
    return [num for num in nums[37:52] if num < 0]