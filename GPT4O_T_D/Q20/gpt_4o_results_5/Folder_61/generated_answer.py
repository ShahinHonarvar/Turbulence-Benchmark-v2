def find_n_th_smallest_num(numbers):
    if len(numbers) < 10:
        raise ValueError('The list must contain at least 10 numbers.')
    sorted_numbers = sorted(numbers[:10])
    return sorted_numbers[9]