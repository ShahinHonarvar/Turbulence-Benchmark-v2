def return_nth_smallest_ascii(s):
    subset = s[:7]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 7:
        return sorted_subset[6]
    else:
        return sorted_subset[-1]