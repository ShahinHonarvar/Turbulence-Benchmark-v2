def filter_chars(s):
    for c in range(ord('a'), ord('i') + 1):
        s = s[:36] + s[36:80].replace(chr(c), '') + s[80:]
    return s