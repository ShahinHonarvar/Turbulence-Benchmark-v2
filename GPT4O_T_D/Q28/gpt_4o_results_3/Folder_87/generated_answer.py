def return_nth_smallest_ascii(s):
    if len(s) < 34:
        return None
    subset = sorted(s[29:34])
    if len(subset) < 5:
        return None
    return subset[4]