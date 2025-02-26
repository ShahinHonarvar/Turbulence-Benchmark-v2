def return_nth_smallest_ascii(s):
    subset = s[50:76]
    sorted_chars = sorted(set(subset))
    return sorted_chars[6]