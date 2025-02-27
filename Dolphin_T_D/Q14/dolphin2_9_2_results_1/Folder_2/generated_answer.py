def find_second_smallest_num(l):
    subset = l[43:87]
    if len(subset) < 2:
        return None
    min_num = min(subset)
    subset.remove(min_num)
    return min(subset) if subset else None