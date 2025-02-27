def find_n_th_smallest_num(numbers):
    if len(numbers) < 10:
        raise ValueError('List must contain at least 10 elements')
    sorted_numbers = sorted(numbers[:10])
    return sorted_numbers[9]