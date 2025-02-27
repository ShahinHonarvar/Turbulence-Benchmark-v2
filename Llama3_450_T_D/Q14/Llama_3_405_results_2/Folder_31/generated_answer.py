def find_second_smallest_num(lst):
    slice_lst = lst[29:94]
    if len(slice_lst) < 2:
        return None
    slice_lst.sort()
    return slice_lst[1]