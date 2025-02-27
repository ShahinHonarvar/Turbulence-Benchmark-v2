def find_n_th_smallest_num(num_list):
    sublist = num_list[299:636]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[11]