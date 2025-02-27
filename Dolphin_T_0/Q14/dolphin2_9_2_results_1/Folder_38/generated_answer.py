def find_second_smallest_num(lst):
    if len(lst) < 51:
        return None
    slice_lst = lst[36:52]
    slice_lst.sort()
    if len(set(slice_lst)) < 2:
        return None
    return slice_lst[1]