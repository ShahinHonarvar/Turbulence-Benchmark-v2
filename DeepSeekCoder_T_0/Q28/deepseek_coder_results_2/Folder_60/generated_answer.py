def return_nth_smallest_ascii(s):
    chars = sorted(s[36:80])
    return chars[11] if len(chars) > 11 else None