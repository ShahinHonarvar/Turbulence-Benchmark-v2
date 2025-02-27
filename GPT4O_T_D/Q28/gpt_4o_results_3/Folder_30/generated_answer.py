def return_nth_smallest_ascii(s):
    subset = sorted(s[50:77])
    return subset[10] if len(subset) >= 11 else None