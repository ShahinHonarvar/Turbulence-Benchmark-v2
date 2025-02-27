def find_second_smallest_num(lst):
    if len(lst) < 37:
        return None
    sliced_list = sorted(lst[33:37])
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]