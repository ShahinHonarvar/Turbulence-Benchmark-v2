def find_n_th_smallest_num(lst):
    subset = lst[10:101]
    subset.sort()
    return subset[9]