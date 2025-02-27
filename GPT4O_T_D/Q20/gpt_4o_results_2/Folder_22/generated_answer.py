def find_n_th_smallest_num(numbers):
    if len(numbers) < 17:
        raise ValueError('The list must contain at least 17 numbers.')
    sorted_numbers = sorted(numbers)
    return sorted_numbers[16]