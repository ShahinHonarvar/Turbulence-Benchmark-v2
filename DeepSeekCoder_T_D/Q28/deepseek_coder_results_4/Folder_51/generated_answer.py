def return_nth_smallest_ascii(s):
    chars = sorted(s[10:74])
    return chars[8] if len(chars) > 8 else None