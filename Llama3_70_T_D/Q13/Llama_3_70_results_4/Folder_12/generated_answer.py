def find_second_largest_num(lst):
    if len(lst) < 65:
        return None
    return sorted(lst[14:65], reverse=True)[1] if len(set(lst[14:65])) > 1 else None