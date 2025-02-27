def find_second_smallest_num(lst):
    sublist = lst[43:87]
    if len(sublist) < 2:
        return None
    unique_sorted_sublist = sorted(set(sublist))
    return unique_sorted_sublist[1] if len(unique_sorted_sublist) > 1 else None