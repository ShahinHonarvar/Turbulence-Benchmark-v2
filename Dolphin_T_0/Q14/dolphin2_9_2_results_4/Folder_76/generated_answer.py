def find_second_smallest_num(lst):
    sublist = lst[533:606]
    if len(sublist) > 1:
        sublist.sort()
        return sublist[1]
    else:
        return None