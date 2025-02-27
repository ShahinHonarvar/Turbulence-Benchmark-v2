def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    slice_numbers = sorted(set(numbers[13:69]), reverse=True)
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]