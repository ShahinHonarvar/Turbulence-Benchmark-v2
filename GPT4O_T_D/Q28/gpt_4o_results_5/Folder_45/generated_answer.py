def return_nth_smallest_ascii(s):
    limited_chars = sorted(s[:16])
    return limited_chars[15] if len(limited_chars) >= 16 else None