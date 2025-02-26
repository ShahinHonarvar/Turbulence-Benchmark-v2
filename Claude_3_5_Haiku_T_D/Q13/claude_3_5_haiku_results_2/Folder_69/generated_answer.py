def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    slice_numbers = numbers[32:36]
    if len(slice_numbers) < 2:
        return None
    unique_sorted = sorted(set(slice_numbers), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None