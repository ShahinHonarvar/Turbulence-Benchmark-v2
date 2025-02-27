def find_second_largest_num(lst):
    subset = lst[14:65]
    if len(subset) < 2:
        return None
    max_num = max(subset)
    subset.remove(max_num)
    second_max = max(subset)
    return second_max if second_max != max_num else None