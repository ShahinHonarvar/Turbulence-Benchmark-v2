def all_neg_ints_exclusive(nums):
    a = [n for n in nums if n < 0 and 70 < nums.index(n) < 98]
    return a or []