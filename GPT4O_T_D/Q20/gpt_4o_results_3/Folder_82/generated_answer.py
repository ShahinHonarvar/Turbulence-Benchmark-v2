def find_n_th_smallest_num(lst):
    if len(lst) < 15:
        return None
    sorted_lst = sorted(lst)
    return sorted_lst[14]