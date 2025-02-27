def find_second_smallest_num(lst):
    if len(lst) < 89:
        return None
    sublist = lst[75:89]
    sublist = [x for x in sublist if isinstance(x, int) or isinstance(x, float)]
    if len(sublist) < 2:
        return None
    sublist = sorted(sublist)
    for i in range(1, len(sublist)):
        if sublist[i] != sublist[0]:
            return sublist[i]
    return None