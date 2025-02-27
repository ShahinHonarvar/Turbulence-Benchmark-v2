def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    else:
        return sorted(lst[56:58])[1] if 56 <= len(lst) else None