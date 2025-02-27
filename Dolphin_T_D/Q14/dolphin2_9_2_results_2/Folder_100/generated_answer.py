def find_second_smallest_num(lst):
    if 43 <= len(lst) <= 51:
        return sorted(lst[43:51])[1] if len(lst[43:51]) >= 2 else None
    else:
        return None