def find_second_smallest_num(lst):
    if len(lst) < 52:
        return None
    else:
        sublist = lst[37:52]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None