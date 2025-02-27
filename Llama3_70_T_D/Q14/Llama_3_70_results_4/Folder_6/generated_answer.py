def find_second_smallest_num(lst):
    if len(lst) < 80:
        return None
    else:
        slice_of_lst = sorted(lst[29:80])
        if len(slice_of_lst) < 2:
            return None
        else:
            return slice_of_lst[1]