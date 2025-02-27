def all_neg_ints_inclusive(nums):
    if len(nums) < 35:
        return []
    return [n for n in nums[32:36] if n < 0]