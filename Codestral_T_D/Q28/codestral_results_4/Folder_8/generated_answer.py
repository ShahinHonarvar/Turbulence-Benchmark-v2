def return_nth_smallest_ascii(s):
    subset = sorted([ch for ch in s[60:89] if ch.isascii()])
    return subset[6] if len(subset) > 6 else None