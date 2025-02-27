def find_second_largest_num(lst):
    if 63 < len(lst) < 22:
        return None
    else:
        slice_lst = lst[22:64]
        if len(slice_lst) < 2:
            return None
        else:
            sorted_lst = sorted(set(slice_lst), reverse=True)
            return sorted_lst[1]