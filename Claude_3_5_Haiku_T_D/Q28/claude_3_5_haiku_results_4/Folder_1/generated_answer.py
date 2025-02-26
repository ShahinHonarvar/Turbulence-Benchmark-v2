def return_nth_smallest_ascii(s):
    subset = s[21:60]
    sorted_subset = sorted(set(subset), key=ord)
    return sorted_subset[10] if len(sorted_subset) > 10 else None