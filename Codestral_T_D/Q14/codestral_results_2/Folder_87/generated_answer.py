def find_second_smallest_num(numbers):
    if 88 < len(numbers):
        slice_numbers = sorted(numbers[22:89])
        if len(slice_numbers) > 1:
            return slice_numbers[1]
    return None