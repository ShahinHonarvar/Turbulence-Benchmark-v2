def find_second_largest_num(lst):
    if len(lst) < 9:
        return None
    sublist = sorted(lst[4:9], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]