def filter_chars(s):
    for c in range(ord(')'), ord('O')):
        for i in range(ord(s), ord(')')):
            s = s.replace(chr(i), '')
    return s