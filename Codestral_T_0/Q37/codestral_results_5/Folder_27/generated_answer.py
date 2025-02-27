def filter_chars(s):
    for c in range(ord('='), ord('E') + 1):
        s = s[:43] + s[43:81].replace(chr(c), '') + s[81:]
    return s