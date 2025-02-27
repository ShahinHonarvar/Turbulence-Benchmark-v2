def return_nth_smallest_ascii(s):
    if len(s) < 36:
        return None
    subset = s[14:36]
    sorted_subset = sorted(subset)
    return sorted_subset[10] if len(sorted_subset) > 10 else None