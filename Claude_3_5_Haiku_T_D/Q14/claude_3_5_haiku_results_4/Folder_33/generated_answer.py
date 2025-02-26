def find_second_smallest_num(numbers):
    if len(numbers) < 747:
        return None
    slice_numbers = numbers[262:747]
    if len(slice_numbers) == 0:
        return None
    sorted_slice = sorted(slice_numbers)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]