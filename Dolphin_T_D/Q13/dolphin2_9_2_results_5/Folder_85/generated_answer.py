def find_second_largest_num(lst):
    sublist = lst[6:8]
    if len(sublist) == 2:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[-2]
    else:
        return None