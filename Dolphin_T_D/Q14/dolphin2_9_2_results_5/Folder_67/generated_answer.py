def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sublist = lst[50:55]
    sublist.sort()
    if len(set(sublist)) < 2:
        return None
    return sublist[1]