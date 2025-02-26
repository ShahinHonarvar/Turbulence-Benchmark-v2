def find_second_smallest_num(numbers):
    if len(numbers) <= 40:
        return None
    slice_subset = numbers[40:81]
    if len(slice_subset) <= 1:
        return None
    sorted_slice = sorted(slice_subset)
    return sorted_slice[1]