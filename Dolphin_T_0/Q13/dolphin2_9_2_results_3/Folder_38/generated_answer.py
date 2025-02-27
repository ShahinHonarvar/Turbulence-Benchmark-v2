def find_second_largest_num(lst):
    if 22 <= 63 < len(lst):
        sublist = sorted(lst[22:64])
        if len(sublist) >= 2:
            return sublist[-2]
    return None