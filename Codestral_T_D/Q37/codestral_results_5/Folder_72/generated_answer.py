def filter_chars(s):
    for c in range(ord('H'), ord('s') + 1):
        s = s.replace(chr(c), '') if 35 <= s.find(chr(c)) <= 51 else s
    return s