def find_second_largest_num(numbers):
    if len(numbers) <= 1 or len(numbers) < 11:
        return None
    slice_subset = numbers[0:11]
    sorted_subset = sorted(slice_subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None