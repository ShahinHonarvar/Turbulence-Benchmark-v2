def return_nth_smallest_ascii(s):
    subset = s[:5]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 5:
        return sorted_subset[4]
    else:
        return sorted_subset[-1]