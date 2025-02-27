def find_second_smallest_num(lst):
    subset = lst[29:80]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    subset.remove(smallest)
    if len(subset) < 2:
        return None
    second_smallest = min(subset)
    return second_smallest