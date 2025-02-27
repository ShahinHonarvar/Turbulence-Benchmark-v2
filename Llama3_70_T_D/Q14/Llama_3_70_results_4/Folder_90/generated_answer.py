def find_second_smallest_num(lst):
    slice_lst = lst[527:539]
    if len(slice_lst) < 2:
        return None
    return sorted(slice_lst)[1]