def filter_chars(s):
    for c in range(ord('!'), ord('s') + 1):
        s = s.replace(chr(c), '') if 86 <= s.find(chr(c)) <= 92 else s
    return s