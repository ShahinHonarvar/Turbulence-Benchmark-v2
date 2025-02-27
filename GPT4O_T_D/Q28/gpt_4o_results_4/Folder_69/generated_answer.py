def return_nth_smallest_ascii(s):
    subset = s[67:78]
    subset_sorted = sorted(subset, key=ord)
    return subset_sorted[6] if len(subset_sorted) >= 7 else None