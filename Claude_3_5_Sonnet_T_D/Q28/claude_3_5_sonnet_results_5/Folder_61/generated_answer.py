def return_nth_smallest_ascii(s):
    subset = s[:10]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 10:
        return sorted_subset[9]
    else:
        return None