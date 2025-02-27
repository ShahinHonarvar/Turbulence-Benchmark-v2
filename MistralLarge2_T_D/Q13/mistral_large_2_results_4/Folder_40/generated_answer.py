def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    subset = sorted(lst[:3], reverse=True)
    return subset[1] if len(subset) > 1 else None