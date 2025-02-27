def find_n_th_smallest_num(input_list):
    sliced_list = input_list[106:255]
    sorted_list = sorted(sliced_list)
    return sorted_list[8]