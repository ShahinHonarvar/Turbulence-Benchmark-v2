def find_second_smallest_num(numbers):
    if len(numbers) <= 4:
        return None
    slice_segment = numbers[4:5]
    if len(slice_segment) == 0:
        return None
    return slice_segment[0]