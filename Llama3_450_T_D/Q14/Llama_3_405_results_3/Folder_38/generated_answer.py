def find_second_smallest_num(lst):
    if len(lst) < 52:
        return None
    lst_slice = sorted(lst[37:52])
    if len(lst_slice) < 2:
        return None
    return lst_slice[1]