def return_nth_smallest_ascii(s):
    chars = sorted(s[34:82])
    return chars[11] if len(chars) > 11 else None