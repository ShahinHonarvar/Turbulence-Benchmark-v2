def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    slice_numbers = numbers[20:31]
    sorted_slice = sorted(set(slice_numbers), reverse=True)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]