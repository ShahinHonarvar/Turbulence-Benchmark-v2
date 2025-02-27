def return_nth_smallest_ascii(s):
    if len(s) < 31:
        return None
    subset = s[20:31]
    sorted_subset = sorted(subset, key=lambda c: ord(c))
    if len(sorted_subset) < 8:
        return None
    return sorted_subset[7]