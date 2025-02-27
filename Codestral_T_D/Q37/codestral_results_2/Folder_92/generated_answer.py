def filter_chars(s):
    for c in range(ord('7'), ord('o') + 1):
        if 4 <= s.find(chr(c)) <= 4:
            s = s.replace(chr(c), '')
    return s