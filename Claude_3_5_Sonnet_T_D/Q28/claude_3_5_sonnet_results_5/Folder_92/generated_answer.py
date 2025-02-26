def return_nth_smallest_ascii(s):
    subset = s[:4]
    sorted_subset = sorted(subset)
    return sorted_subset[3] if len(sorted_subset) >= 4 else None