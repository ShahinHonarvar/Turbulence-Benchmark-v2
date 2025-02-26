def return_nth_smallest_ascii(s):
    subset = s[:14]
    sorted_subset = sorted(subset)
    return sorted_subset[13] if len(sorted_subset) >= 14 else None