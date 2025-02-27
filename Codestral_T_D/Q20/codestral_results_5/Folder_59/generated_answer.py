def find_n_th_smallest_num(numbers):
    if len(numbers) < 12:
        raise ValueError('Input list must contain at least 12 elements')
    sorted_numbers = sorted(numbers[:12])
    return sorted_numbers[11]