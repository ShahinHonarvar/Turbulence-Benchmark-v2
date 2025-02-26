def find_second_largest_num(numbers):
    if len(numbers) < 2 or 90 >= len(numbers):
        return None
    slice_list = numbers[90:91]
    if len(slice_list) == 0:
        return None
    return slice_list[0]