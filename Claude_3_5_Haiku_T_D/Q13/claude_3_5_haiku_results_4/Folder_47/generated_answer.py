def find_second_largest_num(numbers):
    if len(numbers) <= 37:
        return None
    slice_subset = numbers[37:77]
    if len(slice_subset) < 2:
        return None
    unique_sorted_subset = sorted(set(slice_subset), reverse=True)
    return unique_sorted_subset[1] if len(unique_sorted_subset) >= 2 else None