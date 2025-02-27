def return_nth_smallest_ascii(s):
    subset = s[60:89]
    if len(subset) < 7:
        return None
    sorted_subset = sorted(subset, key=ord)
    return sorted_subset[6]