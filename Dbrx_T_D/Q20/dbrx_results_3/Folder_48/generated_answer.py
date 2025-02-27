def find_n_th_smallest_num(lst):
    sorted_lst = sorted(lst[127:849])
    if len(sorted_lst) >= 10:
        return sorted_lst[9]
    else:
        return None