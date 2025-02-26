def return_nth_smallest_ascii(s):
    subset = s[:8]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 8:
        return sorted_subset[7]
    else:
        return None