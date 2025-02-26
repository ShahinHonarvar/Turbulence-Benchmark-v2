def return_nth_smallest_ascii(s):
    subset = s[:7]
    sorted_subset = sorted(subset)
    return sorted_subset[6] if len(sorted_subset) >= 7 else None