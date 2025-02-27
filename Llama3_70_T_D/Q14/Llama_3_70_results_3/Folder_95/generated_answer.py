def find_second_smallest_num(numbers):
    if len(numbers) < 86:
        return None
    slice_numbers = sorted(numbers[75:86])
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]