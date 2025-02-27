def return_nth_smallest_ascii(s):
    chars = sorted(s[34:69])
    if len(chars) < 6:
        return None
    return chars[5]