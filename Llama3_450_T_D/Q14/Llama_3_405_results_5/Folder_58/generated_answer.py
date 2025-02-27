def find_second_smallest_num(lst):
    if len(lst) < 371:
        return None
    sliced_lst = lst[310:371]
    if len(sliced_lst) < 2:
        return None
    sliced_lst.sort()
    return sliced_lst[1]