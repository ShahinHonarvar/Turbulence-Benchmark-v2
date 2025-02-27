def return_nth_smallest_ascii(s):
    limited_chars = s[33:86]
    sorted_chars = sorted(limited_chars, key=ord)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None