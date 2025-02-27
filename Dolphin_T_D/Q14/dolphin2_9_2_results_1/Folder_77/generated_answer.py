def find_second_smallest_num(lst):
    if 639 <= 0 or 975 >= len(lst):
        return None
    sublist = sorted(lst[639:976])
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]