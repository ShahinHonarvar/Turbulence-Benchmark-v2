def all_pos_ints_exclusive(nums):
    pos_nums = [num for num in nums if num > 0 and 57 < num < 84]
    return pos_nums if pos_nums else []