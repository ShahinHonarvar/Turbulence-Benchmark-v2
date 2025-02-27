def return_nth_smallest_ascii(s):
    limited_chars = s[:9]
    sorted_chars = sorted(limited_chars)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None