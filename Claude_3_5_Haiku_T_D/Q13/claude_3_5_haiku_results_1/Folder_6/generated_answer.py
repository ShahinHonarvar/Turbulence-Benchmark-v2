def find_second_largest_num(numbers):
    if len(numbers) <= 11:
        return None
    slice_list = numbers[10:67]
    if len(slice_list) < 2:
        return None
    sorted_slice = sorted(slice_list, reverse=True)
    return sorted_slice[1]