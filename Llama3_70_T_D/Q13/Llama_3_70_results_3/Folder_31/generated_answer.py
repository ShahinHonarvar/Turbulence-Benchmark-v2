def find_second_largest_num(lst):
    slice_lst = lst[75:89]
    if len(slice_lst) < 2:
        return None
    else:
        slice_lst.sort(reverse=True)
        return slice_lst[1]