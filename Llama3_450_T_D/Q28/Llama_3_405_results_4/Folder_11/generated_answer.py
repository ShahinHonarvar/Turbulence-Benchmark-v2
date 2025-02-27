def return_nth_smallest_ascii(s):
    chars = sorted(s[9:60])
    return min(sorted(chars), key=lambda x: ord(x), default=None) if len(chars) < 6 else sorted(chars, key=lambda x: ord(x))[5]