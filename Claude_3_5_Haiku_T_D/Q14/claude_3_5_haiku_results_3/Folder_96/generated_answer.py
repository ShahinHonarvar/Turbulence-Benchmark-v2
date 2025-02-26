def find_second_smallest_num(numbers):
    if not numbers or len(numbers) <= 50:
        return None
    slice_subset = numbers[50:201]
    if len(slice_subset) < 2:
        return None
    sorted_slice = sorted(slice_subset)
    return sorted_slice[1]