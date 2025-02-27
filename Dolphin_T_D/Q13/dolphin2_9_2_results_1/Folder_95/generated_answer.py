def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 85:
        return None
    slice_lst = lst[82:87]
    max_num = max(slice_lst)
    slice_lst.remove(max_num)
    if len(slice_lst) == 0:
        return None
    return max(slice_lst)