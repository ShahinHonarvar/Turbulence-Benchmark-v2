def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    sublist = lst[:3]
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1] if len(sublist) > 1 else None