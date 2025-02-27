def return_nth_smallest_ascii(s):
    chars = sorted(s[10:83])
    return chars[17] if len(chars) > 17 else None