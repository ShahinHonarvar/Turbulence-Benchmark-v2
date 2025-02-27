def find_n_th_smallest_num(numbers_list):
    target_range = numbers_list[365:579]
    target_range.sort()
    return target_range[16]