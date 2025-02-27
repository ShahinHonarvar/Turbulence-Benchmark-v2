def find_n_th_smallest_num(numbers):
    slice_numbers = numbers[43:81]
    sorted_numbers = sorted(slice_numbers)
    return sorted_numbers[5]