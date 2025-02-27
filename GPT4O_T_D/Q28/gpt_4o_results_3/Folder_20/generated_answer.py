def return_nth_smallest_ascii(s):
    chars_in_range = s[25:65]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None