def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    slice_numbers = numbers[22:64]
    if len(slice_numbers) < 2:
        return None
    sorted_slice = sorted(slice_numbers, reverse=True)
    return sorted_slice[1]