def return_nth_smallest_ascii(s):
    chars = sorted(s[28:55])
    return chars[13] if len(chars) > 13 else None