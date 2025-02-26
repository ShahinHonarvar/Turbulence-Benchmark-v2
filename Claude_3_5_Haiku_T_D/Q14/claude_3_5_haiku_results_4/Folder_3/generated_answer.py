def find_second_smallest_num(numbers):
    if len(numbers) <= 27:
        return None
    slice_of_numbers = numbers[27:56]
    if len(slice_of_numbers) < 2:
        return None
    sorted_slice = sorted(set(slice_of_numbers))
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]