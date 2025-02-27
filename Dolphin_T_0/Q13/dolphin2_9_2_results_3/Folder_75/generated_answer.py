def find_second_largest_num(lst):
    sublist = lst[56:58]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]