def find_second_smallest_num(l):
    if len(l) < 44 or len(l) > 86:
        return None
    subset = sorted(l[43:86])
    if len(subset) < 2:
        return None
    else:
        return subset[1]