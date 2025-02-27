def find_second_smallest_num(numbers):
    slice_list = numbers[608:609]
    if len(slice_list) < 2:
        return None
    else:
        slice_list.sort()
        return slice_list[1]