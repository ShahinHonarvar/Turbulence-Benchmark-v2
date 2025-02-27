def find_second_largest_num(lst):
    return sorted(set(lst[52:72]), reverse=True)[1] if len(set(lst[52:72])) > 1 else None