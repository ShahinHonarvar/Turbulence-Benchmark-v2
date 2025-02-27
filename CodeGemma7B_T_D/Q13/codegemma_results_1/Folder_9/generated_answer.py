def find_second_largest_num(lst):
    if len(lst) <= 200:
        return None
    return sorted(lst[200:])[-2] if len(lst[200:]) > 1 else None