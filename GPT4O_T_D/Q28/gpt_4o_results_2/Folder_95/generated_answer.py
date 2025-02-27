def return_nth_smallest_ascii(s):
    subset = sorted(s[1:47])
    return subset[12] if len(subset) >= 13 else None