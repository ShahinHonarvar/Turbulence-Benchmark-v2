def return_nth_smallest_ascii(s):
    subset = s[33:61]
    sorted_chars = sorted(subset)
    return sorted_chars[17] if len(sorted_chars) >= 18 else None