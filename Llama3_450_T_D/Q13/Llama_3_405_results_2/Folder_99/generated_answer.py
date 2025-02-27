def find_second_largest_num(lst):
    if len(lst) < 371:
        return None
    sliced_list = sorted(lst[310:371])
    if len(sliced_list) < 2:
        return None
    return sliced_list[-2]