def find_second_largest_num(numbers):
    if len(numbers) <= 30 or len(numbers) < 201:
        return None
    slice_range = numbers[30:201]
    if len(slice_range) <= 1:
        return None
    unique_sorted = sorted(set(slice_range), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None