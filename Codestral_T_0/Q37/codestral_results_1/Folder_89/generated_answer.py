def filter_chars(s):
    for c in [chr(i) for i in range(ord('!'), ord('@') + 1)]:
        s = s.replace(c, '') if 11 <= s.find(c) <= 32 else s
    return s