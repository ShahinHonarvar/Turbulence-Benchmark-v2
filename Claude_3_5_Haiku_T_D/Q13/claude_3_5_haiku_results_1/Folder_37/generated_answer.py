def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 5:
        return None
    slice_subset = numbers[1:6]
    sorted_subset = sorted(slice_subset, reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]