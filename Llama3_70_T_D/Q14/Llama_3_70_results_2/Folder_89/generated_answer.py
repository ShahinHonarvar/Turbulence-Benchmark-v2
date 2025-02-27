def find_second_smallest_num(lst):
    if len(lst) > 63:
        return sorted(lst[62:64])[1] if len(set(lst[62:64])) > 1 else None
    else:
        return None