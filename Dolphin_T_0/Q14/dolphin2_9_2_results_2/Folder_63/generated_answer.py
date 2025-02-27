def find_second_smallest_num(lst):
    sublist = lst[56:83]
    if len(set(sublist)) < 2:
        return None
    else:
        sublist.sort()
        return sublist[1]