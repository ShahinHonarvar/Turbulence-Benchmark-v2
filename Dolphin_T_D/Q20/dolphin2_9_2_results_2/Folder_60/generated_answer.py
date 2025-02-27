def find_n_th_smallest_num(input_list):
    input_list_filtered = [x for x in input_list[15:74]]
    input_list_filtered.sort()
    return input_list_filtered[14]