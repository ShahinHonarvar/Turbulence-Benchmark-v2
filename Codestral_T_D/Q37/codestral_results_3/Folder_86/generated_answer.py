def filter_chars(s):
    for c in range(ord('O'), ord('}') + 1):
        s = s[:164] + s[164:707].replace(chr(c), '') + s[707:]
    return s