def return_nth_smallest_ascii(s):
    subset = s[12:73]
    sorted_subset = sorted(subset)
    return sorted_subset[12] if len(sorted_subset) > 12 else None