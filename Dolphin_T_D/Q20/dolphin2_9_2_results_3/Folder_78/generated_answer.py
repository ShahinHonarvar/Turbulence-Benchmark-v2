def find_n_th_smallest_num(lst):
    index_start = 16
    index_end = 71
    list_slice = sorted(lst[index_start:index_end + 1])
    n_smallest = 14
    return list_slice[n_smallest - 1]