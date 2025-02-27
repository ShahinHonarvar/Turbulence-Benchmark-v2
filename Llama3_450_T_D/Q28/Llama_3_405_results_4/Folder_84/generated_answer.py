def return_nth_smallest_ascii(s):
    chars = sorted(s[52:80])
    return min(chars, key=lambda x: abs(ord(x) - sorted([ord(c) for c in chars])[6]))