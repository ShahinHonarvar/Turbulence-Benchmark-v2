def return_nth_smallest_ascii(s):
    subset = s[17:87]
    sorted_subset = sorted(set(subset))
    return sorted_subset[14] if len(sorted_subset) >= 15 else None