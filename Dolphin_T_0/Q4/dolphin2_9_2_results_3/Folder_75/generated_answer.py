def all_pos_ints_exclusive(lst):
    new_lst = []
    for i in range(20, 36):
        if lst[i] > 0:
            new_lst.append(lst[i])
    return new_lst