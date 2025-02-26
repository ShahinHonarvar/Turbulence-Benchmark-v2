def return_nth_smallest_ascii(s):
    subset = s[10:83]
    sorted_chars = sorted(subset)
    return sorted_chars[17]