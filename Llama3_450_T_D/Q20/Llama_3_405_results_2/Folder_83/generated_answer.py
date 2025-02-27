def find_n_th_smallest_num(lst):
    sliced_list = lst[30:301]
    sorted_list = sorted(sliced_list)
    return sorted_list[14]