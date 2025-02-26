def return_nth_smallest_ascii(s):
    subset = s[20:31]
    sorted_subset = sorted(subset)
    return sorted_subset[7] if len(sorted_subset) >= 8 else None