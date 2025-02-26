def find_second_smallest_num(numbers):
    if len(numbers) < 83:
        return None
    slice_numbers = numbers[56:83]
    if len(slice_numbers) < 2:
        return None
    sorted_slice = sorted(set(slice_numbers))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None