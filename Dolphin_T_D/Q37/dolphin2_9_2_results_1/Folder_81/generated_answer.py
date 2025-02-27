def filter_chars(s):
    for c in range(ord('8'), ord('m') + 1):
        for i in range(19, 93):
            s = s[:i] + s[i:].replace(chr(c), '')
    return s