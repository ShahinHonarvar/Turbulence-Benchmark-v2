def return_nth_smallest_ascii(s):
    chars = sorted(s[17:57])
    return chars[8] if len(chars) > 8 else None