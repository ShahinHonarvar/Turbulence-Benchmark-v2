def all_pos_ints_exclusive(nums):
    lst = [i for i in nums if i > 0 and i >= 20 and (i < 93)]
    return lst if lst else []