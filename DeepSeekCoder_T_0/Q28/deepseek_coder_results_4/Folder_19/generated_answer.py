def return_nth_smallest_ascii(s):
    chars = sorted(s[0:19])
    return chars[12] if len(chars) > 12 else None