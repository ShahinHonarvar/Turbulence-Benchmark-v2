def find_second_largest_num(lst):
    if not lst or not 40 <= len(lst) <= 80:
        return None
    if len(lst) < 40:
        return None
    sublist = lst[40:80]
    sorted_sublist = sorted(set(sublist), reverse=True)
    if len(sorted_sublist) < 2:
        return None
    else:
        return sorted_sublist[1]