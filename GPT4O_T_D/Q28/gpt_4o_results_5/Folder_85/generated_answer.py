def return_nth_smallest_ascii(s):
    subset = s[17:87]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 15:
        return None
    return sorted_subset[14]