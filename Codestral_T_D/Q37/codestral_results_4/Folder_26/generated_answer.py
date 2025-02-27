def filter_chars(s):
    for i in range(ord('i'), ord('k') + 1):
        s = s[:20] + ''.join((c for c in s[20:63] if ord(c) != i)) + s[63:]
    return s