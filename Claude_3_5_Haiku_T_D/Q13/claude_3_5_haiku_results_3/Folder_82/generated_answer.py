def find_second_largest_num(numbers):
    if len(numbers) < 22:
        return None
    slice_of_numbers = numbers[20:201]
    if not slice_of_numbers:
        return None
    sorted_slice = sorted(slice_of_numbers, reverse=True)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]