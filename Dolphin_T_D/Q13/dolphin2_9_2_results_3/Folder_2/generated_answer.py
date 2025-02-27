def find_second_largest_num(lst):
    if 15 <= len(lst) <= 39:
        return sorted(set(lst[15:40]), reverse=True)[1] if len(set(lst[15:40])) > 1 else None
    else:
        return None