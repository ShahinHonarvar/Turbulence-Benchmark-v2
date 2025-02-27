def find_second_smallest_num(lst):
    if not lst or len(lst) < 2:
        return None
    slice_lst = lst[21:98]
    if len(slice_lst) < 2:
        return None
    slice_lst.sort()
    second_smallest = slice_lst[1]
    return second_smallest