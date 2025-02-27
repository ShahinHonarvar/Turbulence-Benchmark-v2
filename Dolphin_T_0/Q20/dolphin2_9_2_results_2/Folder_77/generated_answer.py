def find_n_th_smallest_num(lst):
    sublst = lst[106:255]
    sublst.sort()
    return sublst[8]