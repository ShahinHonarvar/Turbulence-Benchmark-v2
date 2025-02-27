def find_n_th_smallest_num(lst):
    sub_lst = lst[10:101]
    sub_lst.sort()
    return sub_lst[9]