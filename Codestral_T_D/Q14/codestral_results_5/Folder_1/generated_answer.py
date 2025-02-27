def find_second_smallest_num(numbers):
    if 34 <= len(numbers) <= 55:
        slice_numbers = sorted(numbers[34:56])
        if len(slice_numbers) > 1:
            return slice_numbers[1]
    return None