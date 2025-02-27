def find_second_smallest_num(lst):
    sliced_list = lst[22:89]
    if len(sliced_list) < 2:
        return None
    else:
        sliced_list.sort()
        return sliced_list[1]