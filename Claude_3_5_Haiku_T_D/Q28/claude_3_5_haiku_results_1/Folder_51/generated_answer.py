def return_nth_smallest_ascii(string):
    subset = string[10:74]
    sorted_subset = sorted(set(subset))
    return sorted_subset[8]