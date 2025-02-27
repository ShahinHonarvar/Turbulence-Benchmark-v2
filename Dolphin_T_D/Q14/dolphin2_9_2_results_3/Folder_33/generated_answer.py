def find_second_smallest_num(lst):
    if len(lst) < 746:
        return None
    sublist = lst[262:747]
    if len(sublist) < 2:
        return None
    sublist.sort()
    for i in range(1, len(sublist)):
        if sublist[i] != sublist[i - 1]:
            return sublist[i]
    return None