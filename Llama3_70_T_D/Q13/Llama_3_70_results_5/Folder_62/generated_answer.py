def find_second_largest_num(lst):
    slice_list = lst[91:100]
    if len(slice_list) < 2:
        return None
    slice_list.sort(reverse=True)
    return slice_list[1]