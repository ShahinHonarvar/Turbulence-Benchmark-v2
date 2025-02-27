def find_n_th_smallest_num(numbers):
    if len(numbers) < 16:
        raise ValueError('List must contain at least 16 numbers.')
    sorted_numbers = sorted(numbers)
    return sorted_numbers[15]