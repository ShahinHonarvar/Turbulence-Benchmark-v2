def return_nth_smallest_ascii(s):
    subset = s[50:76]
    sorted_subset = sorted(set(subset))
    return sorted_subset[6] if len(sorted_subset) >= 7 else None