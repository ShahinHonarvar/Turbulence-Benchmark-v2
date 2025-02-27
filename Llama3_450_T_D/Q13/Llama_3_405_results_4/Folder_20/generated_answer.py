def find_second_largest_num(lst):
    if len(lst) < 67:
        return None
    sliced_list = lst[56:67]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    return sliced_list[-2]