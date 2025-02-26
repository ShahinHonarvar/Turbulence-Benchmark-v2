def find_second_largest_num(numbers):
    if len(numbers) <= 200:
        return None
    slice_subset = numbers[200:201]
    if not slice_subset:
        return None
    return slice_subset[0]