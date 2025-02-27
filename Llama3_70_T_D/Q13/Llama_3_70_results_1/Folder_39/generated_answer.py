def find_second_largest_num(numbers):
    slice_numbers = sorted(numbers[20:31])
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[-2]