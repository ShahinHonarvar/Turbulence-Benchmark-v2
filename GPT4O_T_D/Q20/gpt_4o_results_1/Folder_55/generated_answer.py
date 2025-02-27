def find_n_th_smallest_num(numbers):
    if len(numbers) < 13:
        raise ValueError('The list must contain at least 13 distinct numbers.')
    sorted_numbers = sorted(numbers)
    return sorted_numbers[12]