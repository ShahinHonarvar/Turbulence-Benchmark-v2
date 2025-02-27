def find_n_th_smallest_num(numbers_list):
    if len(numbers_list) < 191:
        return None
    sorted_numbers = sorted(numbers_list[18:191])
    return sorted_numbers[18]