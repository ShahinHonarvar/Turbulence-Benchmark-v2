def find_second_smallest_num(lst):
    if 246 > 750 or 750 >= len(lst):
        return None
    sublist = sorted(lst[246:751])
    if len(sublist) < 2:
        return None
    return sublist[1]