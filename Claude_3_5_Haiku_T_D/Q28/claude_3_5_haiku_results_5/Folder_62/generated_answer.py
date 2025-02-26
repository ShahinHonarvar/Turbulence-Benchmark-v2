def return_nth_smallest_ascii(s):
    subset = s[51:79]
    sorted_subset = sorted(set(subset))
    return sorted_subset[8] if len(sorted_subset) >= 9 else None