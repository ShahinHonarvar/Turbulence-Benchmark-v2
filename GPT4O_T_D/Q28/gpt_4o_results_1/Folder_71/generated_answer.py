def return_nth_smallest_ascii(s):
    if len(s) < 83:
        return None
    subset = s[5:83]
    sorted_subset = sorted(subset)
    return sorted_subset[15] if len(sorted_subset) >= 16 else None