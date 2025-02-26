def find_second_smallest_num(lst):
    if len(lst) < 534:
        return None
    sublist = lst[533:606]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None