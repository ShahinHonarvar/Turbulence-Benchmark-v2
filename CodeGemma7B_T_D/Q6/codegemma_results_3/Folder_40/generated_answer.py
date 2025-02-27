def all_neg_ints_exclusive(nums):
    return [num for num in nums if num in range(-2, 0) and num not in [0]]