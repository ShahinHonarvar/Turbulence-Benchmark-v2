def all_neg_ints_inclusive(nums):
    return [num for i, num in enumerate(nums[:5]) if i < 5 and num < 0]