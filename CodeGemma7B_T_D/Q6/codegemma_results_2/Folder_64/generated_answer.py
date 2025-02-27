def all_neg_ints_exclusive(nums):
    return [num for num in nums if num < 0 and num != 0 and (num <= 4)]