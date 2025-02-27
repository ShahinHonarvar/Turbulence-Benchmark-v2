def find_second_smallest_num(lst):
    slice_lst = lst[50:201]
    if len(slice_lst) < 2:
        return None
    min1 = min(slice_lst)
    slice_lst.remove(min1)
    if len(slice_lst) < 1:
        return None
    min2 = min(slice_lst)
    return min2