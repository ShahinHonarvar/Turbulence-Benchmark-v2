def find_second_largest_num(lst):
    sublist = lst[661:925]
    sorted_sublist = sorted(set(sublist), reverse=True)
    if len(sorted_sublist) < 2:
        return None
    else:
        return sorted_sublist[1]