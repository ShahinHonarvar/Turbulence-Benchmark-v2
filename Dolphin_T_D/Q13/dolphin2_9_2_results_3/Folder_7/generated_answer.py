def find_second_largest_num(lst):
    if len(lst) < 661 or len(lst) > 924:
        return None
    sublist = lst[661:925]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]