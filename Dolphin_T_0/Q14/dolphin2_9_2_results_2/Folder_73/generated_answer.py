def find_second_smallest_num(lst):
    if 59 <= len(lst) <= 97:
        return sorted(lst[59:98])[1] if len(lst[59:98]) > 1 else None
    else:
        return None