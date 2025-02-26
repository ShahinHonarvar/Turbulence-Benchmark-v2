def return_nth_smallest_ascii(s):
    subset = s[:46]
    sorted_subset = sorted(set(subset))
    return sorted_subset[9] if len(sorted_subset) >= 10 else None