def filter_chars(s):
    for c in range(ord('P'), ord('x') + 1):
        if 12 <= s.find(chr(c)) <= 25:
            s = s.replace(chr(c), '')
    return s