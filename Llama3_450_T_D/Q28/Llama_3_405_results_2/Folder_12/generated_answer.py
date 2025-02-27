def return_nth_smallest_ascii(s):
    chars = sorted(s[3:27])
    return min(chars, key=lambda x: (ord(x), [ord(c) for c in chars].index(ord(x))), reverse=False)