def all_neg_ints_exclusive(nums):
    result = [num for i, num in enumerate(nums) if i + 1 > 10 and i + 1 < 100 and (num < 0)]
    return result