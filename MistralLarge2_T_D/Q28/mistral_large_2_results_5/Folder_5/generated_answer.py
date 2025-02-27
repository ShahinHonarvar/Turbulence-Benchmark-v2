def return_nth_smallest_ascii(s):
    subset = s[5:90]
    sorted_chars = sorted(subset)
    return sorted_chars[12] if len(sorted_chars) > 12 else None