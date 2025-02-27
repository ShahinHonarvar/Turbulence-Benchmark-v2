def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    sublist = lst[56:58]
    if len(sublist) < 2:
        return None
    sorted_list = sorted(set(sublist))
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]