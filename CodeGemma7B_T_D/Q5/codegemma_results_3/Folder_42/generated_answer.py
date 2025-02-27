def all_neg_ints_inclusive(nums):
    return nums[29:79 + 1] if any((n < 0 for n in nums[29:79 + 1])) else []