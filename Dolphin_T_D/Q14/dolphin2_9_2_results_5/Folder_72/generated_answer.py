def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sublist = lst[82:87]
    sublist = sorted(sublist)
    if len(sublist) < 2:
        return None
    return sublist[1]