def find_second_largest_num(lst):
    slice_lst = lst[30:201]
    slice_lst.sort(reverse=True)
    if len(slice_lst) < 2:
        return None
    return slice_lst[1]