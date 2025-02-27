def find_n_th_smallest_num(num_list):
    n = 7
    start = 15
    end = 24
    sublist = sorted(num_list[start:end + 1])
    return sublist[n - 1]