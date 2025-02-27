def return_nth_smallest_ascii(s):
    subset = s[58:86]
    sorted_subset = sorted(subset, key=ord)
    return sorted_subset[18] if len(sorted_subset) > 19 else None