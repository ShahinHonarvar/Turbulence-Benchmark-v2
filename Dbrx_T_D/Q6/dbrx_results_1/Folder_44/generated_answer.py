def all_neg_ints_exclusive(nums):
    start, end = (81, 86)
    return [n for n in nums[start:end] if n < 0]