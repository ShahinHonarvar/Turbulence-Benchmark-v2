def find_n_th_smallest_num(numbers_list):
    start_index = 470
    end_index = 654
    sub_list = sorted(numbers_list[start_index:end_index + 1])
    return sub_list[8]