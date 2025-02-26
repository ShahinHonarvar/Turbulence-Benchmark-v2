def find_second_largest_num(numbers):
    if len(numbers) < 25 or 23 >= len(numbers):
        return None
    slice_subset = numbers[23:24]
    if not slice_subset:
        return None
    return slice_subset[0]