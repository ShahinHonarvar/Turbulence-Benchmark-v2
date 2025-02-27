def return_nth_smallest_ascii(s):
    chars = sorted(s[10:74])
    return min(chars, key=lambda c: abs(ord(c) - sorted(map(ord, chars))[8]))