def filter_chars(s):
    for c in range(ord('b') + 1, ord('d') - 1):
        s = s.replace(chr(c), '')
    return s