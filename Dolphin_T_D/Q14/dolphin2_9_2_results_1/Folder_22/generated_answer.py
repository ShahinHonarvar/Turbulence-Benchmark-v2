def find_second_smallest_num(lst):
    if 200 < len(lst) < 40:
        return None
    sublist = lst[40:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]