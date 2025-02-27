def return_nth_smallest_ascii(s):
    chars = sorted(s[60:84])
    return min(chars, key=lambda c: (ord(c), chars.index(c)))[13]