def return_nth_smallest_ascii(s):
    subset = s[36:80]
    sorted_subset = sorted(set(subset))
    return sorted_subset[11] if len(sorted_subset) >= 12 else None