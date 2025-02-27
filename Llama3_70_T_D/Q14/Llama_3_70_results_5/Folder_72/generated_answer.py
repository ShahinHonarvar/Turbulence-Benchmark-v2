def find_second_smallest_num(lst):
    second_smallest = None
    if len(lst) > 86:
        slice_lst = lst[82:87]
        slice_lst.sort()
        if len(slice_lst) > 1:
            second_smallest = slice_lst[1]
    return second_smallest