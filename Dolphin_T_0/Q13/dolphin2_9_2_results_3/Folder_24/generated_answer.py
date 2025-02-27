def find_second_largest_num(lst):
    sublist = lst[74:96]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[-2]