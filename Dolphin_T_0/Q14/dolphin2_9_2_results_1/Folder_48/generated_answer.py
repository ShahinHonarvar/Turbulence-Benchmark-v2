def find_second_smallest_num(l):
    sublist = l[246:751]
    if len(sublist) < 2:
        return None
    sublist.sort()
    for i in range(1, len(sublist)):
        if sublist[i] != sublist[0]:
            return sublist[i]
    return None