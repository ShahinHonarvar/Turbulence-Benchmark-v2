def return_nth_smallest_ascii(s):
    subset = sorted(s[17:87])
    if len(subset) < 15:
        return None
    return subset[14]