def return_nth_smallest_ascii(s):
    limited_chars = s[:13]
    sorted_chars = sorted(limited_chars)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None