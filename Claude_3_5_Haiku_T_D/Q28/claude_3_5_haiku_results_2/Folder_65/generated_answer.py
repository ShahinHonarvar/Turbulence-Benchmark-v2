def return_nth_smallest_ascii(s):
    subset = [char for char in s[32:68]]
    sorted_subset = sorted(subset)
    return sorted_subset[11] if len(sorted_subset) >= 12 else None