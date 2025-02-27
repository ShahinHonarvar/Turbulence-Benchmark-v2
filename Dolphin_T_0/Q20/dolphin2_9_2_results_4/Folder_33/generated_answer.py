def find_n_th_smallest_num(arr):
    sliced_arr = arr[213:323]
    n_th_num = sorted(sliced_arr)[7]
    return n_th_num