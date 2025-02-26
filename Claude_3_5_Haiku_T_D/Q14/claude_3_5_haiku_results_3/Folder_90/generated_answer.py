def find_second_smallest_num(numbers):
    if len(numbers) <= 527:
        return None
    slice_range = numbers[527:539]
    if len(slice_range) < 2:
        return None
    try:
        sorted_slice = sorted(slice_range)
        return sorted_slice[1]
    except Exception:
        return None