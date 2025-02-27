def find_second_largest_num(lst):
    if 639 <= 975 < len(lst):
        sublist = sorted(lst[639:976], reverse=True)
        if len(sublist) >= 2:
            return sublist[1]
    return None