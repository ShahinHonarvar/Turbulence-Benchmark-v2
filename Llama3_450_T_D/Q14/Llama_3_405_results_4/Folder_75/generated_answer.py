def find_second_smallest_num(lst):
    if len(lst) < 93:
        return None
    sliced_list = sorted(lst[12:93])
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]