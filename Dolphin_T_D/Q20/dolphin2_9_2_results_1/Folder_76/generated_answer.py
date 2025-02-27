def find_n_th_smallest_num(lst):
    sub_lst = lst[260:823]
    sub_lst.sort()
    return sub_lst[10 - 1]