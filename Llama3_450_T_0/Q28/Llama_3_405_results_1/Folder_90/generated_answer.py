def return_nth_smallest_ascii(s):
    chars = sorted(s[17:84])
    return min(chars, key=lambda x: (ord(x), chars.index(x) >= 4))