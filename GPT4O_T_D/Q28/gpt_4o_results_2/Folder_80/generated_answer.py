def return_nth_smallest_ascii(s):
    if len(s) < 90:
        return None
    subset = s[51:90]
    sorted_chars = sorted(subset)
    if len(sorted_chars) < 14:
        return None
    return sorted_chars[13]