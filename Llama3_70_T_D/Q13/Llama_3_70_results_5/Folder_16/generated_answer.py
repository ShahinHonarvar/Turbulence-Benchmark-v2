def find_second_largest_num(lst):
    slice_ = lst[33:37]
    unique_slice = sorted(set(slice_))
    if len(unique_slice) < 2:
        return None
    return unique_slice[-2]