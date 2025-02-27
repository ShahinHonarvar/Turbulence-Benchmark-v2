def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 51:
        return None
    return sorted(lst[43:51])[1] if len(set(lst[43:51])) > 1 else None