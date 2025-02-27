def find_n_th_smallest_num(num_list):
    num_list.sort()
    sliced_list = num_list[43:81]
    n_th_smallest_num = sliced_list[5]
    return n_th_smallest_num