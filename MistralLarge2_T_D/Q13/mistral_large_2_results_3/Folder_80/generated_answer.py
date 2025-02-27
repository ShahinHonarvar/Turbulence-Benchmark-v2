def find_second_largest_num(lst):
    if len(lst) < 67:
        return None
    subset = sorted(lst[64:67], reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]