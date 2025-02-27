def all_pos_ints_exclusive(nums):
    return [x for x in nums if 0 <= x < 100 and x not in range(33, 100)]