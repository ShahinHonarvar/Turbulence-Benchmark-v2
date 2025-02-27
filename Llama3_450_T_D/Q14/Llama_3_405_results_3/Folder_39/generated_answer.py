def find_second_smallest_num(lst):
    if len(lst) < 29 or len(lst) < 41:
        sliced_list = lst[28:]
    else:
        sliced_list = lst[28:41]
    if len(sliced_list) < 2:
        return None
    else:
        sliced_list.sort()
        return sliced_list[1]