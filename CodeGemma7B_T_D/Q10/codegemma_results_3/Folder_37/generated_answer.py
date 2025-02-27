def all_odd_ints_exclusive(nums):
    return [i for i in nums if i % 2 != 0 and 1 < i < nums.index(i)] or []