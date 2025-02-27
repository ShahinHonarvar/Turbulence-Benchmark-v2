def find_second_smallest_num(lst):
    if 31 <= len(lst) < 34:
        return None
    sublist = lst[31:35]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None