def find_second_smallest_num(lst):
    if not lst:
        return None
    slice_lst = lst[80:201]
    if len(slice_lst) < 2:
        return None
    mins = sorted(slice_lst[:2])
    lst_set = set(slice_lst)
    for num in slice_lst[2:]:
        if num < mins[1] and num not in mins:
            mins[1] = num
    return mins[1] if mins[1] in lst_set else None