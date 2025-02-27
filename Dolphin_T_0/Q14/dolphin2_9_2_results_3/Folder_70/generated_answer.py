def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    elif len(lst) < 49:
        return None
    sublist = lst[35:50]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    second_min = sorted(unique_sublist)[1]
    return second_min