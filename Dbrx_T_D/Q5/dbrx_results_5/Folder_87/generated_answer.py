def all_neg_ints_inclusive(nums):
    if len(nums) < 46:
        return []
    return [n for n in nums[36:47] if n < 0]