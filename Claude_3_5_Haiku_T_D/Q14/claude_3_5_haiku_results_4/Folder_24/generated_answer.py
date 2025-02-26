def find_second_smallest_num(numbers):
    if len(numbers) <= 23:
        return None
    slice_sublist = numbers[23:24]
    if not slice_sublist:
        return None
    return slice_sublist[0]