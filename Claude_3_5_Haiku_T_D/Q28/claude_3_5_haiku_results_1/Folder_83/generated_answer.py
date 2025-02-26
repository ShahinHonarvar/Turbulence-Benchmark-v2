def return_nth_smallest_ascii(s):
    subset = s[30:71]
    sorted_subset = sorted(subset)
    return sorted_subset[14] if len(sorted_subset) >= 15 else None