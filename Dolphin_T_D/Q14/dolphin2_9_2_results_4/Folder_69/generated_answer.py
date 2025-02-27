def find_second_smallest_num(lst):
    if len(lst) == 0 or len(lst) < 88:
        return None
    else:
        sublist = lst[25:88]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]