def return_nth_smallest_ascii(s):
    chars = sorted(s[18:46])
    return chars[6] if len(chars) > 6 else None