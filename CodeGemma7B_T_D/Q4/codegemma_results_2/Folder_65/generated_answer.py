def all_pos_ints_exclusive(nums):
    return [n for n in nums if isinstance(n, int) and n > 0 and (42 < n < 87)]