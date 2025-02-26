def return_nth_smallest_ascii(s):
    subset = s[13:36]
    sorted_subset = sorted(set(subset), key=ord)
    return sorted_subset[17] if len(sorted_subset) >= 18 else None