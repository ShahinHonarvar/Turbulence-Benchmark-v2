def filter_chars(s):
    for c in range(ord('c'), ord('n') + 1):
        s = s[:13] + s[13:29].replace(chr(c), '') + s[29:]
    return s