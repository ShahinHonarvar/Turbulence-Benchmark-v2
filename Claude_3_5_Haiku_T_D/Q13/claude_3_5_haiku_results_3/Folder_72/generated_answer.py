def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    slice_numbers = numbers[29:52]
    if len(slice_numbers) == 0:
        return None
    sorted_slice = sorted(slice_numbers, reverse=True)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]