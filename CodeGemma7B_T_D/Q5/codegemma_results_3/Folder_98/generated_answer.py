def all_neg_ints_inclusive(nums):
    if all((n >= 0 for n in nums[0:7])):
        return []
    return [n for n in nums[0:7] if n < 0]