def return_nth_smallest_ascii(s):
    limited_string = s[:88]
    sorted_chars = sorted(limited_string)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None