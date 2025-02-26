def find_second_largest_num(numbers):
    if len(numbers) < 23:
        return None
    slice_range = numbers[22:51]
    if len(slice_range) == 0:
        return None
    unique_sorted = sorted(set(slice_range), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None