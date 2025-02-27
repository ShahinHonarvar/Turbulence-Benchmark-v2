def find_n_th_smallest_num(input_list, low=23, high=45, n=7):
    subset = sorted(input_list[low:high + 1])
    return subset[n - 1]