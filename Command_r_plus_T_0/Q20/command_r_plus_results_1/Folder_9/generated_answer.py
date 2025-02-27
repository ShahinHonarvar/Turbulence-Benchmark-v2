def find_n_th_smallest_num(numbers_list):
    if len(numbers_list) < 101:
        return None
    sorted_numbers = sorted(numbers_list[10:101])
    return sorted_numbers[9]