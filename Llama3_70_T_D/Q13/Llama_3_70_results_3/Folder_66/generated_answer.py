def find_second_largest_num(lst):
    slice_of_lst = lst[50:55]
    if len(slice_of_lst) < 2:
        return None
    else:
        slice_of_lst.sort(reverse=True)
        return slice_of_lst[1]