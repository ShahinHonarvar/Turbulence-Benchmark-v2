def return_nth_smallest_ascii(s):
    chars = sorted(s[10:74])
    return min(chars, key=lambda x: (ord(x), chars.index(x)))[8]