def find_second_smallest_num(lst):
    if len(lst) <= 200:
        return None
    slice_lst = lst[49:201]
    if len(slice_lst) <= 2:
        return None
    slice_lst.sort()
    return slice_lst[1]