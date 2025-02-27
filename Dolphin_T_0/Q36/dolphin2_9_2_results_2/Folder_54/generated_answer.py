def filter_chars(s):
    for c in range(ord(')'), ord('P')):
        s = s.replace(chr(c), '')
    return s