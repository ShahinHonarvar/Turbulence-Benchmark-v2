def return_nth_smallest_ascii(s):
    subset = s[:16]
    sorted_subset = sorted(subset)
    return sorted_subset[15] if len(sorted_subset) >= 16 else None