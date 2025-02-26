def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    slice_numbers = numbers[29:52]
    if len(slice_numbers) < 2:
        return None
    sorted_slice = sorted(slice_numbers, reverse=True)
    return sorted_slice[1]