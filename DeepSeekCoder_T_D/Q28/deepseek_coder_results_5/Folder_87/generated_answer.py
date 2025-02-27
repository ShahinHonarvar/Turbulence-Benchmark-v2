def return_nth_smallest_ascii(s):
    subset = sorted(s[29:34])
    return subset[4] if len(subset) > 4 else None