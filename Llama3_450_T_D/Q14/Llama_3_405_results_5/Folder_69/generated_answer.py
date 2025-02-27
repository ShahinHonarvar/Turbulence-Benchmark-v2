def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    slice_of_numbers = numbers[25:88]
    sorted_slice = sorted(slice_of_numbers)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]