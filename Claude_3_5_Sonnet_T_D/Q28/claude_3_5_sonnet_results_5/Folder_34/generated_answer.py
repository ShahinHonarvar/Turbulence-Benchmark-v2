def return_nth_smallest_ascii(s):
    subset = s[:19]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 19:
        return sorted_subset[18]
    else:
        return None