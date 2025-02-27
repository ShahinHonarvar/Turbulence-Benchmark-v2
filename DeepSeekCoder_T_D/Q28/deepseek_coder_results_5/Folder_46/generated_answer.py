def return_nth_smallest_ascii(s):
    chars = sorted(s[34:86])
    return chars[19] if len(chars) > 19 else None