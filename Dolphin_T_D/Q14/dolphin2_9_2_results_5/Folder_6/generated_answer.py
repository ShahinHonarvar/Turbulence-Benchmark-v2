def find_second_smallest_num(lst):
    subset = lst[29:80]
    if len(subset) < 2:
        return None
    first_min = min(subset)
    subset.remove(first_min)
    if len(subset) == 0:
        return None
    second_min = min(subset)
    return second_min