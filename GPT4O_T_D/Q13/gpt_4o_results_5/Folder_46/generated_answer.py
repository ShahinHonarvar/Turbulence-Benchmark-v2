def find_second_largest_num(lst):
    if len(lst) < 88:
        return None
    sublist = lst[30:88]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort()
    return unique_sublist[-2]