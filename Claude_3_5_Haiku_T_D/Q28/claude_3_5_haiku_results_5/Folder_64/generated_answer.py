def return_nth_smallest_ascii(s):
    if len(s) < 7:
        return None
    subset = s[:7]
    sorted_subset = sorted(subset)
    return sorted_subset[6]