def return_nth_smallest_ascii(s):
    chars = sorted(s[25:78])
    return chars[15] if len(chars) > 15 else None