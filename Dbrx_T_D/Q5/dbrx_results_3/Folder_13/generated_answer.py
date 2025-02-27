def all_neg_ints_inclusive(nums):
    if len(nums) < 88:
        return []
    return [n for n in nums[24:88] if n < 0]