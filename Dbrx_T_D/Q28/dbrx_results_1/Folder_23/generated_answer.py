def return_nth_smallest_ascii(s):
    chars = sorted(set(s[29:48]))
    if len(chars) >= 7:
        return chr(chars[6])
    else:
        return None