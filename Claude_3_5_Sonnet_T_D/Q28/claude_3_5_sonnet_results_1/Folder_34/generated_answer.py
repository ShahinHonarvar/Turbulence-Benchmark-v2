def return_nth_smallest_ascii(s):
    subset = s[:19]
    sorted_subset = sorted(subset)
    return sorted_subset[18] if len(sorted_subset) >= 19 else None