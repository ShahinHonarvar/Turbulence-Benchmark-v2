def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 9:
        return None
    slice_subset = numbers[0:10]
    sorted_subset = sorted(slice_subset)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    return None