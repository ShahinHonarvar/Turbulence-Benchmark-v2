def return_nth_smallest_ascii(s):
    subset = s[:13]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 13:
        return sorted_subset[12]
    return None