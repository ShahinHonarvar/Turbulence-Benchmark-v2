def filter_chars(s):
    for char in range(ord('E'), ord('G') + 1):
        s = s.replace(chr(char), '')
    return s