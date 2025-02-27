def find_n_th_smallest_num(lst):
    sub_lst = lst[299:636]
    sub_lst.sort()
    return sub_lst[11]