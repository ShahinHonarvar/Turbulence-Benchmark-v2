def find_n_th_smallest_num(numbers):
    sliced_numbers = numbers[20:63]
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[11]