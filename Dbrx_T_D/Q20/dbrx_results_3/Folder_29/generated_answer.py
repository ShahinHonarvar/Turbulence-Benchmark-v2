def find_n_th_smallest_num(numbers):
    numbers_to_consider = numbers[20:63]
    sorted_numbers = sorted(numbers_to_consider)
    return sorted_numbers[11]