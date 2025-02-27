def find_n_th_smallest_num(lst):
    sub_lst = lst[33:95]
    sub_lst.sort()
    return sub_lst[17] if len(sub_lst) > 18 else None