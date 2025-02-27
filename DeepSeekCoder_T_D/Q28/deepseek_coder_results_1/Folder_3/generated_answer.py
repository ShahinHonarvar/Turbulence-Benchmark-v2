def return_nth_smallest_ascii(s):
    chars = sorted(s[25:46])
    return chars[10] if len(chars) > 10 else None