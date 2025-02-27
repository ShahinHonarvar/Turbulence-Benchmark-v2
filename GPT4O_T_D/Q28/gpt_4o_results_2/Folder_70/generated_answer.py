def return_nth_smallest_ascii(s):
    subset = s[28:55]
    sorted_subset = sorted(subset)
    return sorted_subset[13] if len(sorted_subset) > 13 else None