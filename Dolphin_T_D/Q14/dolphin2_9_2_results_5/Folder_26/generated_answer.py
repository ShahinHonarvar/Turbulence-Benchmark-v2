def find_second_smallest_num(lst):
    sublist = lst[62:79]
    if len(sublist) >= 2:
        sublist.sort()
        return sublist[1]
    else:
        return None