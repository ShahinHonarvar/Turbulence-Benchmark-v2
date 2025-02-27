def all_neg_ints_exclusive(nums):
    return [n for n in nums if n < 0 and 20 < nums.index(n) < 51]