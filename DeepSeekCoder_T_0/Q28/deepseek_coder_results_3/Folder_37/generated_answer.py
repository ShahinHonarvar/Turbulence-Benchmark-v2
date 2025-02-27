def return_nth_smallest_ascii(s):
    chars = sorted(s[28:68])
    return chars[14] if len(chars) > 14 else None