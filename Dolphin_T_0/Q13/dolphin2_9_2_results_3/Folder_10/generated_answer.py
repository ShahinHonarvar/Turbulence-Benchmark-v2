def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    sublist = lst[25:60]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort()
    return unique_sublist[-2]