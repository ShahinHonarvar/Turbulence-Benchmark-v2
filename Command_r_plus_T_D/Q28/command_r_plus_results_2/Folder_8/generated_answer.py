def return_nth_smallest_ascii(s: str) -> str:
    subset = s[60:89]
    sorted_subset = sorted(subset)
    return sorted_subset[6]