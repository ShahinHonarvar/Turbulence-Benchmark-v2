def return_nth_smallest_ascii(s):
    chars = sorted(s[42:60])
    return chars[16] if len(chars) > 16 else None