def find_second_largest_num(lst):
    if len(lst) < 2 or len(lst) < 88 - 30:
        return None
    else:
        sublist = lst[30:88]
        sublist.sort()
        sublist.reverse()
        return sublist[1]