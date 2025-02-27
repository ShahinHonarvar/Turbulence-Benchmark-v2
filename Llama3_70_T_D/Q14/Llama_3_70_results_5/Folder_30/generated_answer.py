def find_second_smallest_num(lst):
    if len(lst) < 53:
        return None
    slice_of_lst = lst[26:53]
    if len(slice_of_lst) < 2:
        return None
    slice_of_lst.sort()
    return slice_of_lst[1]