def find_second_largest_num(lst):
    if len(lst) < 98:
        return None
    sliced_list = lst[21:98]
    sliced_list.sort(reverse=True)
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]