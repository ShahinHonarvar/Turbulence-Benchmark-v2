def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    slice_lst = lst[4:8]
    if len(set(slice_lst)) < 2:
        return None
    slice_lst.sort()
    return slice_lst[1]