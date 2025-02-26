def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    slice_section = numbers[35:50]
    if len(slice_section) < 2:
        return None
    sorted_slice = sorted(set(slice_section), reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None