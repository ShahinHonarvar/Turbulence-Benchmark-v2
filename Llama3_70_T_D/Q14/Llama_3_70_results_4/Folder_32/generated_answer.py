def find_second_smallest_num(lst):
    if len(lst) < 36:
        return None
    slice_lst = sorted(lst[32:36])
    if len(slice_lst) < 2:
        return None
    return slice_lst[1]