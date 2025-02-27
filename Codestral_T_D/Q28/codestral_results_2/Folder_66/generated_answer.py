def return_nth_smallest_ascii(s):
    chars = sorted(s[35:53])
    if len(chars) < 10:
        return None
    else:
        return chars[9]