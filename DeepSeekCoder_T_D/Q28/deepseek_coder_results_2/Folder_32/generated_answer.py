def return_nth_smallest_ascii(s):
    chars = sorted(s[14:67])
    return chars[7] if len(chars) > 7 else None