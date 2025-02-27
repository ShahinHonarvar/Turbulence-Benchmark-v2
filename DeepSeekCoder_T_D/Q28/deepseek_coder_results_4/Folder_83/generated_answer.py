def return_nth_smallest_ascii(s):
    chars = sorted(s[30:71])
    return chars[14] if len(chars) > 14 else None