def filter_chars(s):
    for char in range(ord('S'), ord('s') + 1):
        s = s.replace(chr(char), '')
    return s