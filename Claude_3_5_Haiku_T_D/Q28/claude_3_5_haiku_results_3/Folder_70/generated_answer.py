def return_nth_smallest_ascii(s):
    subset = s[28:55]
    sorted_subset = sorted(set(subset))
    return sorted_subset[13]