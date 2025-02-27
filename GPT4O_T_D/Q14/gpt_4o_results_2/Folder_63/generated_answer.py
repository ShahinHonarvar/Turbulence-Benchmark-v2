def find_second_smallest_num(lst):
    sublist = lst[56:83]
    if len(sublist) < 2:
        return None
    sorted_unique_sublist = sorted(set(sublist))
    if len(sorted_unique_sublist) < 2:
        return None
    return sorted_unique_sublist[1]