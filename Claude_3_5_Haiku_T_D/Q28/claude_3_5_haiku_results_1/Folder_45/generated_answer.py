def return_nth_smallest_ascii(s):
    if len(s) <= 15:
        return min(s)
    subset = s[:16]
    sorted_subset = sorted(subset)
    return sorted_subset[15]