def find_second_largest_num(lst):
    sublist = lst[3:6]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[-2]