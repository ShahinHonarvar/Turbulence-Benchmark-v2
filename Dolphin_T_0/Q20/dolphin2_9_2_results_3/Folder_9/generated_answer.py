def find_n_th_smallest_num(lst):
    sublist = lst[10:101]
    sublist.sort()
    return sublist[9]