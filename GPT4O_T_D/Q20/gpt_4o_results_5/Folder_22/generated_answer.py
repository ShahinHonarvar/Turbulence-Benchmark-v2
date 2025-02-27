def find_n_th_smallest_num(numbers):
    if len(numbers) < 17:
        raise ValueError('List must contain at least 17 numbers.')
    return sorted(numbers)[16]