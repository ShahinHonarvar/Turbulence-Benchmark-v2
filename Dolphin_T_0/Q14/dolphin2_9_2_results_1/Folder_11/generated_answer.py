def find_second_smallest_num(lst):
    if len(lst) < 66:
        return None
    slice_lst = lst[66:94]
    if len(slice_lst) < 2:
        return None
    min_elem = min(slice_lst)
    slice_lst.remove(min_elem)
    if len(slice_lst) < 2:
        return None
    sec_min_elem = min(slice_lst)
    return sec_min_elem