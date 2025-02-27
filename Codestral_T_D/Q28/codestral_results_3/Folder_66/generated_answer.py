def return_nth_smallest_ascii(s):
    subset = sorted(s[35:53])
    return subset[9] if len(subset) > 10 else None