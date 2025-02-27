def find_n_th_smallest_num(input_list):
    start_index = 4
    end_index = 7
    mini_list = sorted(input_list[start_index:end_index + 1])
    return mini_list[3]