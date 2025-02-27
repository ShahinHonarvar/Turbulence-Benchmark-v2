def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    return sorted(lst[:5])[4] if len(set(lst[:5])) > 1 else None