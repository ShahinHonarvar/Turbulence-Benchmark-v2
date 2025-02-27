def find_second_smallest_num(lst):
    if len(lst) < 49:
        return None
    slice_lst = lst[34:50]
    if len(set(slice_lst)) < 2:
        return None
    sorted_slice_lst = sorted(set(slice_lst))
    for num in sorted_slice_lst[1:]:
        return num