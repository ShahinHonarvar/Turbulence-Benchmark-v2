def find_n_th_smallest_num(numbers):
    if not isinstance(numbers, list) or len(numbers) < 45:
        raise ValueError('Input list must have at least 46 distinct numbers')
    slice_numbers = numbers[23:46]
    return sorted(slice_numbers)[6]