def return_nth_smallest_ascii(s):
    chars = sorted(s[6:59])
    if len(chars) >= 19:
        return chars[18]
    else:
        return None