def filter_chars(s):
    for c in range(ord('6'), ord('A') + 1):
        s = s.replace(chr(c), '')
    for i in range(138, 921):
        if s[i] in map(chr, range(ord('6'), ord('A') + 1)):
            s = s[:i] + s[i + 1:]
    return s