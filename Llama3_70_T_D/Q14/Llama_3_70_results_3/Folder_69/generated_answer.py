def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    slice_numbers = numbers[25:88]
    sorted_slice_numbers = sorted(slice_numbers)
    if len(sorted_slice_numbers) < 2:
        return None
    return sorted_slice_numbers[1]