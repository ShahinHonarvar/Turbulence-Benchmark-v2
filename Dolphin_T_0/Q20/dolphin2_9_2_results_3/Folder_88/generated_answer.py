def find_n_th_smallest_num(lst):
    lst_slice = lst[1:9]
    sorted_lst = sorted(lst_slice)
    return sorted_lst[7]