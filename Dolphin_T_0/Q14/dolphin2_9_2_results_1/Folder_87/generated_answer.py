def find_second_smallest_num(lst):
    if len(lst) < 89 or len(lst) > 22:
        return None
    slice_lst = lst[22:89]
    if len(set(slice_lst)) < 2:
        return None
    slice_lst.sort()
    return slice_lst[1]