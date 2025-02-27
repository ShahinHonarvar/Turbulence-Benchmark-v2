def find_n_th_smallest_num(numbers_list):
    if len(numbers_list) < 86:
        return None
    sub_list = sorted(numbers_list[69:86])
    return sub_list[6]