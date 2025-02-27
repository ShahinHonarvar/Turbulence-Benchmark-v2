def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    slice_lst = lst[4:5]
    if len(slice_lst) < 2:
        return None
    return sorted(slice_lst)[1]