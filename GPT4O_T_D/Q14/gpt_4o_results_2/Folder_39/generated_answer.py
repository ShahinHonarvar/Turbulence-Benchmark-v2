def find_second_smallest_num(lst):
    sublist = lst[28:41]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]