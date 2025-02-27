def return_nth_smallest_ascii(s):
    subset = sorted(s[58:86])
    return subset[18] if len(subset) > 18 else None