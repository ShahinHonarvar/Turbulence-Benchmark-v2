def all_pos_ints_inclusive(lst):
    target_lst = []
    for i in range(40, 201):
        if lst[i] > 0:
            target_lst.append(lst[i])
    return target_lst