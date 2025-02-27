def find_second_largest_num(l):
    if 310 <= 370 < len(l):
        sublist = l[310:371]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[-2]
    return None