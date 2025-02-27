def all_neg_ints_inclusive(nums):
    if len(nums) < 10:
        return []
    return [n for n in nums[8:10] if n < 0]