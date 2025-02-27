def find_n_th_smallest_num(lst):
    sub_lst = lst[23:58]
    sub_lst.sort()
    return sub_lst[4 - 1]