def find_second_smallest_num(lst):
    subset = lst[4:9]
    if len(subset) < 2:
        return None
    else:
        subset.remove(min(subset))
        return min(subset)