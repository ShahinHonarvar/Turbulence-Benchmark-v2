def filter_chars(s):
    for c in [chr(i) for i in range(ord('O'), ord('^') + 1)]:
        s = s[:17] + s[17:64].replace(c, '') + s[64:]
    return s