def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    sublist = sorted(lst[5:9])
    if len(sublist) < 2:
        return None
    return sublist[1]