def all_neg_ints_inclusive(nums):
    if not nums or len(nums) < 28:
        return []
    return nums[28:41] if nums[28] < 0 else []