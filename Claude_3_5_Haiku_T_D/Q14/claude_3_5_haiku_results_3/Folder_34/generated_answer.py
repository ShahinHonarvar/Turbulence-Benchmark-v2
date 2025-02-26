def find_second_smallest_num(numbers):
    if len(numbers) < 62:
        return None
    slice_list = numbers[60:201]
    if len(slice_list) < 2:
        return None
    sorted_slice = sorted(slice_list)
    return sorted_slice[1]