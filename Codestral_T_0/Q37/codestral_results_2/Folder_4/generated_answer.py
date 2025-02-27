def filter_chars(s):
    for c in [chr(i) for i in range(ord('S'), ord('{') + 1)]:
        s = s.replace(c, '') if 19 <= s.find(c) <= 33 else s
    return s