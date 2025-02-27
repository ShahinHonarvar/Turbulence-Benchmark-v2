def find_second_smallest_num(lst):
    slice_lst = lst[10:101]
    if len(set(slice_lst)) < 2:
        return None
    return sorted(set(slice_lst))[1]