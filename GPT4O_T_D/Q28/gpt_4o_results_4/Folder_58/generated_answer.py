def return_nth_smallest_ascii(s):
    subset = s[8:27]
    sorted_subset = sorted(subset)
    return sorted_subset[5] if len(sorted_subset) >= 6 else None