def find_second_smallest_num(lst):
    if len(lst) < 24:
        return None
    s = sorted(lst[23:25])
    return s[1] if len(s) > 1 else None