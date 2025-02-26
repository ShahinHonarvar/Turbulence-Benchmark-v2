def return_nth_smallest_ascii(s):
    subset = s[1:47]
    sorted_subset = sorted(set(subset))
    return sorted_subset[12] if len(sorted_subset) >= 13 else None