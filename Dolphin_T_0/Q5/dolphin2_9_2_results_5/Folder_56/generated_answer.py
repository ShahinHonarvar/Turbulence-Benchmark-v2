def all_neg_ints_inclusive(nums):
    if len(nums) > 0 and nums[0] < 0:
        return [nums[0]]
    else:
        return []