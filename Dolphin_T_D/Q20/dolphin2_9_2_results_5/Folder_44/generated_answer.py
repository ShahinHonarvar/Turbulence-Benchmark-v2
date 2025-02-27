def find_n_th_smallest_num(num_list):
    sublist = num_list[23:58]
    sublist.sort()
    return sublist[4 - 1]