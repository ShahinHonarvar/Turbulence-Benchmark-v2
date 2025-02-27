def return_nth_smallest_ascii(s):
    chars = s[12:56]
    ascii_values = [ord(c) for c in chars]
    t = sorted(ascii_values)
    if len(t) < 17:
        return None
    else:
        return chr(t[16])