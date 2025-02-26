def find_second_smallest_num(numbers):
    if len(numbers) <= 86:
        return None
    slice_range = numbers[68:87]
    if not slice_range:
        return None
    unique_sorted = sorted(set(slice_range))
    return unique_sorted[1] if len(unique_sorted) > 1 else None