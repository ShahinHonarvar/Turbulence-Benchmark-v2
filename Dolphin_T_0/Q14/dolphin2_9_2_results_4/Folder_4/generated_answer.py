def find_second_smallest_num(lst):
    sublist = lst[70:85]
    sublist.sort()
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None