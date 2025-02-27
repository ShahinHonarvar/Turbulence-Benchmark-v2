def return_nth_smallest_ascii(s):
    subset = s[51:90]
    if len(subset) < 14:
        return None
    sorted_chars = sorted(subset)
    return sorted_chars[13]