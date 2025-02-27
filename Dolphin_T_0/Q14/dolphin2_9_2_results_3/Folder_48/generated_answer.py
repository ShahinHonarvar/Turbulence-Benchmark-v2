def find_second_smallest_num(lst):
    if 246 <= 750 < len(lst):
        sublist = sorted(lst[246:751])
        if len(sublist) > 1:
            return sublist[1]
    return None