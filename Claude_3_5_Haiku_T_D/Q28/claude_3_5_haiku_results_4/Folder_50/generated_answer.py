def return_nth_smallest_ascii(s):
    subset = s[25:89]
    sorted_chars = sorted(set(subset))
    return sorted_chars[10]