def return_nth_smallest_ascii(s):
    chars = sorted(s[22:75])
    return chars[11] if len(chars) > 11 else None