def find_second_largest_num(numbers):
    if len(numbers) < 22:
        return None
    slice_section = numbers[20:31]
    sorted_slice = sorted(slice_section, reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None