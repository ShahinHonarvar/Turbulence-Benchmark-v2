def find_second_smallest_num(lst):
    if len(lst) < 35:
        return None
    slice_lst = lst[31:35]
    if len(set(slice_lst)) < 2:
        return None
    sorted_slice = sorted(set(slice_lst))
    return sorted_slice[1]