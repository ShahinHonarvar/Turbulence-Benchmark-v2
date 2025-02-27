def return_nth_smallest_ascii(s):
    limited_chars = s[32:68]
    sorted_chars = sorted(limited_chars, key=ord)
    return sorted_chars[11] if len(sorted_chars) >= 12 else None