def find_second_smallest_num(lst):
    sublist = lst[75:95]
    sublist = list(set(sublist))
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]