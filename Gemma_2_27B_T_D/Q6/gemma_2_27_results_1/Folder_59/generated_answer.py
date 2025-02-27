def all_neg_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if num < 0 and 0 <= i < 10]