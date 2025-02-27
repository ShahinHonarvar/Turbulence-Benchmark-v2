def find_second_largest_num(lst):
    if not 12 <= len(lst) <= 92:
        return None
    else:
        sublist = lst[12:93]
        if len(set(sublist)) < 2:
            return None
        else:
            return sorted(sublist)[-2]