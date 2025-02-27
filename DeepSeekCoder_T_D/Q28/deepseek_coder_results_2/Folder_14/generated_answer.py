def return_nth_smallest_ascii(s):
    chars = sorted(s[46:83])
    return chars[15] if len(chars) > 15 else None