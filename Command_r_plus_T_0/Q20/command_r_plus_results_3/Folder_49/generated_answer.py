def find_n_th_smallest_num(numbers):
    sliced_numbers = numbers[20:201]
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[10]