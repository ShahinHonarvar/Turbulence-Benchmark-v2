def find_n_th_smallest_num(numbers_list):
    if len(numbers_list) < 74:
        return None
    sorted_list = sorted(numbers_list[15:74])
    return sorted_list[14]