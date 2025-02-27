def find_second_smallest_num(lst):
    if 79 < len(lst) < 29:
        return None
    else:
        return sorted(lst[29:80])[1] if len(lst[29:80]) > 1 else None