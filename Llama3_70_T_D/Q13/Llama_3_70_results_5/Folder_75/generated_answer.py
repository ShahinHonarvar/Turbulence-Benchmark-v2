def find_second_largest_num(lst):
    if len(lst) < 58:
        return None
    slice_lst = lst[56:58]
    slice_lst.sort(reverse=True)
    if len(slice_lst) < 2:
        return None
    return slice_lst[1]