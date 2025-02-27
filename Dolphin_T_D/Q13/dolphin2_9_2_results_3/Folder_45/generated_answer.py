def find_second_largest_num(numbers_list):
    if 200 < len(numbers_list) < 30:
        return None
    slice_list = numbers_list[30:201]
    if len(set(slice_list)) < 2:
        return None
    first_max = max(slice_list)
    slice_list.remove(first_max)
    second_max = max(slice_list)
    return second_max