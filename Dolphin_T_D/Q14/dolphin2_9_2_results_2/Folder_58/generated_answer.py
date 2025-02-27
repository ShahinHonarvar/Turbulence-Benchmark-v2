def find_second_smallest_num(lst):
    if 310 <= 370 < len(lst):
        sublist = sorted(lst[310:371])
        if len(sublist) > 1:
            return sublist[1]
    return None