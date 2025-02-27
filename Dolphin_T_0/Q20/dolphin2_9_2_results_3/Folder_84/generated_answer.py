def find_n_th_smallest_num(lst):
    windows = [7, 32]
    sublist = lst[windows[0]:windows[1] + 1]
    sublist.sort()
    return sublist[6]