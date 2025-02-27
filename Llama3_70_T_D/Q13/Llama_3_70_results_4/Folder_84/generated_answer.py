def find_second_largest_num(lst):
    if 43 > len(lst) - 1 or 86 > len(lst) - 1:
        return None
    else:
        return sorted(lst[43:87], reverse=True)[1]