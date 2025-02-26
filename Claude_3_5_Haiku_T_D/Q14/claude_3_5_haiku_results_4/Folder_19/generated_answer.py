def find_second_smallest_num(numbers):
    if len(numbers) <= 8:
        return None
    slice_list = numbers[4:9]
    if len(slice_list) < 2:
        return None
    sorted_slice = sorted(slice_list)
    return sorted_slice[1]