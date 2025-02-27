def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    if 86 < len(lst):
        lst = lst[82:87]
    lst.sort()
    if len(lst) < 2:
        return None
    return lst[1]