def find_second_largest_num(numbers):
    if len(numbers) < 54:
        return None
    slice_subset = numbers[52:72]
    sorted_slice = sorted(slice_subset, reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None