def find_n_th_smallest_num(num_list):
    if len(num_list) < 7:
        raise ValueError('Input list must contain at least 7 distinct numbers.')
    sorted_list = sorted(num_list[0:8])
    return sorted_list[7]