def find_second_largest_num(lst):
    slice_lst = lst[5:8]
    sorted_slice_lst = sorted(slice_lst, reverse=True)
    if len(sorted_slice_lst) < 2:
        return None
    else:
        return sorted_slice_lst[1]