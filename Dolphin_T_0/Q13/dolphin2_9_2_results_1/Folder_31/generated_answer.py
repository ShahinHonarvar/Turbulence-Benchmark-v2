def find_second_largest_num(lst):
    subset = lst[75:89]
    if len(set(subset)) < 2:
        return None
    else:
        return sorted(set(subset))[-2]