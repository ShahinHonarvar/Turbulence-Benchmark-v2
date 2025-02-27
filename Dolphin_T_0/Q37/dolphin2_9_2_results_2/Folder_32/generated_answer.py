def filter_chars(s):
    for char in range(ord('w'), ord('{' + 1)):
        s = s.replace(chr(char), '')
    return s