def find_second_smallest_num(lst):
    if len(lst) < 79:
        return None
    sublist = lst[29:80]
    if len(set(sublist)) < 2:
        return None
    sublist.sort()
    return sublist[1]