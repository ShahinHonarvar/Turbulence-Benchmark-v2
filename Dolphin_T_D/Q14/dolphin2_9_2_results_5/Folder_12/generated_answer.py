def find_second_smallest_num(lst):
    if len(lst) < 72 or len(lst) > 31:
        return None
    slice_lst = lst[31:72]
    if len(set(slice_lst)) < 2:
        return None
    slice_lst.sort()
    return slice_lst[1]