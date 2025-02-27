def find_n_th_smallest_num(numbers_list):
    trimmed_list = numbers_list[25:91]
    fourth_smallest = sorted(trimmed_list)[3]
    return fourth_smallest