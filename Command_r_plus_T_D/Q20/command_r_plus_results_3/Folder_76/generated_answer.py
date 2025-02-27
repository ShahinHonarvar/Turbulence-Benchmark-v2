def find_n_th_smallest_num(numbers_list):
    start_index = 260
    end_index = 822
    if len(numbers_list[start_index:end_index + 1]) < 10:
        return None
    numbers_list_slice = sorted(numbers_list[start_index:end_index + 1])
    return numbers_list_slice[9]