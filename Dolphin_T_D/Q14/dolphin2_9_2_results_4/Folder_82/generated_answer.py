def find_second_smallest_num(lst):
    if len(lst) < 20:
        return None
    sublist = lst[20:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]