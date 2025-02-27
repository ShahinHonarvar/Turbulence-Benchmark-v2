def return_nth_smallest_ascii(s):
    subset = s[29:48]
    sorted_subset = sorted(subset, key=lambda c: ord(c))
    return sorted_subset[6] if len(sorted_subset) >= 7 else None