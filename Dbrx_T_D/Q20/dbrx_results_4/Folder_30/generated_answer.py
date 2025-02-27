def find_n_th_smallest_num(numbers):
    if len(numbers) <= 99 or len(numbers) < 78:
        raise IndexError('Input list is too short.')
    return sorted(numbers[78:100])[18]