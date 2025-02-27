def find_second_smallest_num(lst):
    sublist = lst[52:72]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1] if len(set(sublist)) > 1 else None