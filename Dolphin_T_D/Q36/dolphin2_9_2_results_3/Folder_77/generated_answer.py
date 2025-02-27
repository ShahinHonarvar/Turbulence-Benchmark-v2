def filter_chars(s):
    for char in range(ord('-'), ord('v') + 1):
        s = s.replace(chr(char), '')
    return s