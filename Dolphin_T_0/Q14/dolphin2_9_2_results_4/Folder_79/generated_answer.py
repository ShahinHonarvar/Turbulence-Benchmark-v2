def find_second_smallest_num(lst):
    sublist = lst[1:6]
    if len(sublist) >= 2:
        sublist.sort()
        return sublist[1]
    else:
        return None