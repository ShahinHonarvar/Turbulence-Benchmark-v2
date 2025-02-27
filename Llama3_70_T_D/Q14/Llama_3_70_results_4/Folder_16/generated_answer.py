def find_second_smallest_num(numbers):
    if len(numbers) < 78:
        return None
    slice_numbers = sorted(numbers[66:78])
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]