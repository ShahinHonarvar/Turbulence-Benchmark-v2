def return_nth_smallest_ascii(s):
    subset = s[67:78]
    sorted_subset = sorted(subset, key=ord)
    return sorted_subset[6] if len(sorted_subset) >= 7 else None