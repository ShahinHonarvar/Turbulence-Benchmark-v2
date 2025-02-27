def find_second_smallest_num(lst):
    sublist = sorted(lst[29:80])
    if len(sublist) < 2:
        return None
    return sublist[1]