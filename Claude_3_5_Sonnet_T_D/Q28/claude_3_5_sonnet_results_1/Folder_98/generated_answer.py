def return_nth_smallest_ascii(s):
    subset = s[:9]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 9:
        return sorted_subset[8]
    else:
        return None