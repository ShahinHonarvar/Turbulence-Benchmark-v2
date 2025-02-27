def find_second_smallest_num(lst):
    if 52 <= len(lst) <= 71:
        sublist = lst[52:72]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[1]
    return None