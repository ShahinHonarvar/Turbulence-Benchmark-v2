def find_n_th_smallest_num(lst):
    subarray = lst[2:8]
    subarray.sort()
    return subarray[3]