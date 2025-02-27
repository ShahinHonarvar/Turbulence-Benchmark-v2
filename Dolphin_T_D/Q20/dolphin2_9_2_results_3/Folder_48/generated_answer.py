def find_n_th_smallest_num(lst, n=10):
    sublist = sorted(lst[127:849])
    return sublist[n - 1]