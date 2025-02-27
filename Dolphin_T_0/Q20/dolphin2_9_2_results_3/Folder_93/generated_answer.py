def find_n_th_smallest_num(lst):
    sublist = lst[40:100]
    sublist = list(set(sublist))
    sublist.sort()
    return sublist[5]