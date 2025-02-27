def find_second_smallest_num(lst):
    if len(lst) <= 10:
        return None
    else:
        return sorted(lst[10:11])[1] if len(sorted(lst[10:11])) > 1 else None