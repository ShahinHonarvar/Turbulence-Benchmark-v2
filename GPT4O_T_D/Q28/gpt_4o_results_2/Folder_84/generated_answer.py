def return_nth_smallest_ascii(s):
    if len(s) < 80:
        return None
    subset = s[52:80]
    sorted_subset = sorted(subset)
    return sorted_subset[6] if len(sorted_subset) >= 7 else None