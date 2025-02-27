def return_nth_smallest_ascii(s):
    chars = [c for c in s[35:53] if c.isprintable()]
    chars.sort(key=ord)
    return chars[9]