def return_nth_smallest_ascii(s):
    if len(s) < 46:
        return None
    subset = s[18:46]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 7:
        return None
    return sorted_subset[6]