def return_nth_smallest_ascii(s):
    chars = sorted(s[5:48])
    return chars[12] if len(chars) > 12 else None