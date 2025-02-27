def return_nth_smallest_ascii(s):
    chars = sorted(s[47:81])
    return chars[3] if len(chars) > 3 else None