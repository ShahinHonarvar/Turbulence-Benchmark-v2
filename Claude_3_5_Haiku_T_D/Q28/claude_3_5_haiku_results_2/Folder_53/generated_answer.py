def return_nth_smallest_ascii(s):
    subset = s[40:61]
    sorted_subset = sorted(set(subset))
    return sorted_subset[18]