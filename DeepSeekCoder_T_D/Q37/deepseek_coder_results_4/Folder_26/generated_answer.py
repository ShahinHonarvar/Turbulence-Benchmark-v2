def filter_chars(s):
    for i in range(ord('i'), ord('k') + 1):
        s = s.replace(chr(i), '')
    return s