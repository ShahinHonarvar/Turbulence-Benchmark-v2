def find_second_smallest_num(lst):
    if len(lst) < 67:
        return None
    slice_lst = lst[64:67]
    slice_lst.sort()
    if len(slice_lst) < 2:
        return None
    return slice_lst[1]