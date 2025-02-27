def find_n_th_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    slice_numbers = sorted(numbers[2:9])
    return slice_numbers[4]