def find_second_largest_num(lst):
    slice_list = sorted(lst[28:39], reverse=True)
    if len(slice_list) < 2:
        return None
    else:
        return slice_list[1]