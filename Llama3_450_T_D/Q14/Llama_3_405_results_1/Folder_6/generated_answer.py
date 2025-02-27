def find_second_smallest_num(lst):
    if len(lst) < 80:
        return None
    sliced_list = lst[29:80]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort()
    return sliced_list[1]