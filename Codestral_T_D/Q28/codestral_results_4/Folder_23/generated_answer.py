def return_nth_smallest_ascii(s):
    subset = sorted(s[29:48])
    return subset[6] if len(subset) > 6 else None