def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    slice_numbers = sorted(numbers[12:93])
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]