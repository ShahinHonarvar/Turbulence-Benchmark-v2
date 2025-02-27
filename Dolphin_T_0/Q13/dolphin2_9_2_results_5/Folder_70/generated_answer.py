def find_second_largest_num(lst):
    subset = lst[28:33]
    if len(set(subset)) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)