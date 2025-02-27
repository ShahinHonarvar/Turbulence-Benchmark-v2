def find_second_smallest_num(lst):
    lst = lst[82:87]
    if len(lst) < 2:
        return None
    else:
        return sorted(lst)[1]