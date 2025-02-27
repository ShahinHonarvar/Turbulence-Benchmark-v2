def find_n_th_smallest_num(input_list):
    relevant_slice = input_list[63:80]
    relevant_slice.sort()
    return relevant_slice[10]