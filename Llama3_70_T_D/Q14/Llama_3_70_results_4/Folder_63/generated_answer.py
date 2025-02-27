def find_second_smallest_num(numbers):
    if 82 < len(numbers):
        slice_numbers = sorted(numbers[56:83])
        if len(slice_numbers) > 1:
            return slice_numbers[1]
    return None