def return_nth_smallest_ascii(s):
    subset = s[:5]
    sorted_subset = sorted(subset)
    return sorted_subset[4] if len(sorted_subset) >= 5 else None