def find_second_smallest_num(lst):
    if 16 < len(lst) < 79:
        sublist = lst[16:79]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None