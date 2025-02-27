def find_n_th_smallest_num(lst):
    del lst[:145]
    del lst[12:]
    return sorted(lst)[5]