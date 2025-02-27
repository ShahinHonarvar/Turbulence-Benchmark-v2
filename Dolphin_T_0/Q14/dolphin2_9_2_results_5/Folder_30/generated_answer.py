def find_second_smallest_num(lst):
    sublist = lst[25:53]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]