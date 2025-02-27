def return_nth_smallest_ascii(s):
    subset = sorted(s[12:56])
    return subset[16] if len(subset) >= 17 else None