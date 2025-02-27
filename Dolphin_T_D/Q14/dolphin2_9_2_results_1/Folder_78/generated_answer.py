def find_second_smallest_num(lst):
    if not 17 <= len(lst) <= 78:
        return None
    slice_lst = lst[17:79]
    if len(set(slice_lst)) == 1:
        return None
    slice_lst.sort()
    return slice_lst[1]