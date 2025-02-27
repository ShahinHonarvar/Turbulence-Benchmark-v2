def find_n_th_smallest_num(lst):
    sorted_lst = sorted(lst[:7])
    return sorted_lst[6] if len(sorted_lst) == 7 else None