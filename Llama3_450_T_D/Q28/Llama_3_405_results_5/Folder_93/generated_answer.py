def return_nth_smallest_ascii(s):
    chars = sorted(s[42:60])
    return min(chars, key=lambda x: abs(ord(x) - sorted([ord(c) for c in chars])[16]))