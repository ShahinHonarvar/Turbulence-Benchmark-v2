def return_nth_smallest_ascii(s):
    subset = s[25:65]
    sorted_subset = sorted(set(subset))
    return sorted_subset[5] if len(sorted_subset) >= 6 else None