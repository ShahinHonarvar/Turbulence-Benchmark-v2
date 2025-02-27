def filter_chars(s):
    for c in range(ord('!'), ord('*')):
        if any([s[i] == chr(c) for i in range(82, 93)]):
            s = s.replace(chr(c), '')
    return s