def all_pos_ints_exclusive(lst):
    pos_nums = []
    for i in range(4):
        if lst[i] > 0:
            pos_nums.append(lst[i])
    return pos_nums