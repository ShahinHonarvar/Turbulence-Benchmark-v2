def find_second_smallest_num(lst):
    slice_lst = lst[661:925]
    if len(slice_lst) < 2:
        return None
    else:
        slice_lst.sort()
        return slice_lst[1]