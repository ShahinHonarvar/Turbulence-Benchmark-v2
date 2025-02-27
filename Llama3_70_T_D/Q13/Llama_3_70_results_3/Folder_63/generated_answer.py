def find_second_largest_num(lst):
    slice_of_list = lst[22:89]
    if len(slice_of_list) < 2:
        return None
    return sorted(set(slice_of_list), reverse=True)[1]