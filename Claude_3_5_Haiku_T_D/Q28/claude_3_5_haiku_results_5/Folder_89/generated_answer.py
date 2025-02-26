def return_nth_smallest_ascii(s):
    subset = s[24:72]
    sorted_subset = sorted(set(subset))
    return sorted_subset[7]