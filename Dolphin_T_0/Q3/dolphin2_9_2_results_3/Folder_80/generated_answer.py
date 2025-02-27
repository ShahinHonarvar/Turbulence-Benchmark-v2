def all_pos_ints_inclusive(lst):
    sub_lst = []
    for i in range(64, 67):
        if i < len(lst) and lst[i] > 0:
            sub_lst.append(lst[i])
    return sub_lst