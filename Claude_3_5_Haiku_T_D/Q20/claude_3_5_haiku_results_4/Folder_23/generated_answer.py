def find_n_th_smallest_num(numbers):
    selected_range = numbers[14:97]
    sorted_range = sorted(selected_range)
    return sorted_range[12]