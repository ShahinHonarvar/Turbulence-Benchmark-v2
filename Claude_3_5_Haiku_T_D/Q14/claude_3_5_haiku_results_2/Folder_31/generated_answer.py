def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 30:
        return None
    slice_of_numbers = numbers[29:94]
    if len(slice_of_numbers) < 2:
        return None
    sorted_slice = sorted(slice_of_numbers)
    return sorted_slice[1]