def return_nth_smallest_ascii(s):
    chars = sorted(s[12:73])
    return chars[12] if len(chars) > 12 else None