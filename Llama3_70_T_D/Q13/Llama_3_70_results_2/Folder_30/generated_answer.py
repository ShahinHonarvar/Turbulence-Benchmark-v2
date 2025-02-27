def find_second_largest_num(lst):
    if len(lst) < 99:
        return None
    else:
        slice_of_lst = lst[55:99]
        sorted_slice = sorted(set(slice_of_lst), reverse=True)
        if len(sorted_slice) < 2:
            return None
        else:
            return sorted_slice[1]