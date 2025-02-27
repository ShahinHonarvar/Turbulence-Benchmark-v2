def find_second_smallest_num(lst):
    subset = [x for i, x in enumerate(lst) if 91 <= i <= 99]
    if len(subset) < 2:
        return None
    subset.sort()
    for i in subset:
        if subset.count(i) > 1:
            subset.remove(i)
    if len(subset) > 1:
        return subset[1]
    else:
        return None