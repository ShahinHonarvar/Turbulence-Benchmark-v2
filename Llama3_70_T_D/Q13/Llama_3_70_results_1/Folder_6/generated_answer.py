def find_second_largest_num(lst):
    if len(lst) < 67:
        return None
    slice_lst = lst[10:67]
    slice_lst = list(set(slice_lst))
    if len(slice_lst) < 2:
        return None
    return sorted(slice_lst)[-2]