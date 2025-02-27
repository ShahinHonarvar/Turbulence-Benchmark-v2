def return_nth_smallest_ascii(s):
    subset = sorted(s[47:71])
    return subset[13] if len(subset) > 13 else None