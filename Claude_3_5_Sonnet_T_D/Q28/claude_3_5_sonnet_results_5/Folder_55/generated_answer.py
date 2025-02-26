def return_nth_smallest_ascii(s):
    subset = s[:13]
    sorted_subset = sorted(subset)
    return sorted_subset[12] if len(sorted_subset) >= 13 else None