def return_nth_smallest_ascii(s):
    subset = sorted(s[46:83])
    return subset[15] if len(subset) >= 16 else None