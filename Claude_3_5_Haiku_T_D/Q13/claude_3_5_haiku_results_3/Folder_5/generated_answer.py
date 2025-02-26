def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    slice_range = numbers[8:10]
    if len(slice_range) < 2:
        return None
    return sorted(slice_range, reverse=True)[1]