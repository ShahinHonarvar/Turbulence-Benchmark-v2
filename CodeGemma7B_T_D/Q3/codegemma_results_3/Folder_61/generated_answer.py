def all_pos_ints_inclusive(lst):
    pos_nums = []
    for i in range(8):
        if i in lst and i >= 0:
            pos_nums.append(i)
    return pos_nums