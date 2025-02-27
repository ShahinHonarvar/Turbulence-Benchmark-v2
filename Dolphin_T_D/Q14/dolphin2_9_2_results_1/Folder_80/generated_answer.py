def find_second_smallest_num(lst):
    if len(lst) < 88:
        return None
    sublist = lst[30:88]
    if len(set(sublist)) < 2:
        return None
    sublist.sort()
    return sublist[1]