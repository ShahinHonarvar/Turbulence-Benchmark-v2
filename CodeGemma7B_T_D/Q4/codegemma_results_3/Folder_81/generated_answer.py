def all_pos_ints_exclusive(nums):
    return [n for n in nums if n > 0 and 0 < n <= 100 and (n not in range(11, 101))]