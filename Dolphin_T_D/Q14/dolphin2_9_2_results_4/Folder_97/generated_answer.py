def find_second_smallest_num(lst):
    slice_lst = lst[31:35]
    if len(slice_lst) == 0:
        return None
    else:
        return sorted(slice_lst)[1]