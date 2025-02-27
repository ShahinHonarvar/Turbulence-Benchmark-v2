def find_second_smallest_num(lst):
    if len(lst) < 99:
        return None
    sliced_lst = lst[56:99]
    sorted_lst = sorted(sliced_lst)
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]