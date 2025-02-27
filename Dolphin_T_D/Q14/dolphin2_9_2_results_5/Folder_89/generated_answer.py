def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    sublist = lst[62:64]
    if len(sublist) < 2 or sublist[0] == sublist[1]:
        return None
    return min(sublist[1:]) if sublist[0] < sublist[1] else min(sublist[:-1])