def find_second_smallest_num(numbers):
    if len(numbers) <= 4:
        return None
    slice_subset = numbers[4:5]
    if not slice_subset:
        return None
    return slice_subset[0]