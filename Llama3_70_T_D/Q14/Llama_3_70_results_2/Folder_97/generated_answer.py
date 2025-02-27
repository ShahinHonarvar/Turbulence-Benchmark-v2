def find_second_smallest_num(lst):
    slice_lst = lst[31:35]
    slice_lst.sort()
    if len(slice_lst) < 2:
        return None
    return slice_lst[1]