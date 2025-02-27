def find_second_smallest_num(lst):
    if len(lst) < 200:
        return None
    sublist = lst[60:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]