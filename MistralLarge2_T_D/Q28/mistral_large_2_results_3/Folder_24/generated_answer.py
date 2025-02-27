def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[34:82])
    return sorted_chars[11] if len(sorted_chars) >= 12 else None