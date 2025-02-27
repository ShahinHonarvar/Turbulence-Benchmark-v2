def return_nth_smallest_ascii(s):
    chars = sorted(s[18:46])
    return min(chars, key=lambda c: (ord(c), chars.index(c)))[6]