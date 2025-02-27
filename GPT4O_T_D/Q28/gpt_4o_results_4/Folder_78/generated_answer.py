def return_nth_smallest_ascii(s):
    limited_s = s[:88]
    sorted_chars = sorted(limited_s)
    return sorted_chars[13] if len(sorted_chars) > 13 else None