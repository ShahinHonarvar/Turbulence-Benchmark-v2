def find_second_smallest_num(lst):
    sublist = lst[5:7]
    if len(sublist) == 2 and len(set(sublist)) == 2:
        sublist.sort()
        return sublist[1]
    else:
        return None