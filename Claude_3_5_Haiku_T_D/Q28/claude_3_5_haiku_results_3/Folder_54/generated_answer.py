def return_nth_smallest_ascii(s):
    subset = s[12:88]
    sorted_subset = sorted(set(subset))
    return sorted_subset[16]