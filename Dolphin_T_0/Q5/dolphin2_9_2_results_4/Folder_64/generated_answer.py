def all_neg_ints_inclusive(nums):
    neg_nums = [num for num in nums[:5] if num < 0]
    return neg_nums if neg_nums else []