def all_pos_ints_inclusive(lst):
    new_lst = []
    for i in range(3):
        if lst[i] > 0:
            new_lst.append(lst[i])
    return new_lst