def return_nth_smallest_ascii(s):
    chars = sorted(s[37:60])
    return chars[5] if len(chars) > 5 else None