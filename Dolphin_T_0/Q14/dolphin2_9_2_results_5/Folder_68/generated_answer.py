def find_second_smallest_num(lst):
    if not isinstance(lst, list) or len(lst) == 0:
        return None
    elif len(lst) <= 8:
        return sorted(lst)[1] if len(set(lst)) >= 2 else None
    else:
        return sorted(lst[:9])[1] if len(set(lst[:9])) >= 2 else None