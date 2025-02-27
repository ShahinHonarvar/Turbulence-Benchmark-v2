def return_nth_smallest_ascii(s):
    chars = sorted(s[13:36])
    if len(chars) < 18:
        return None
    return chars[17]