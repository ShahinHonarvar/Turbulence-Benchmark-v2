def filter_chars(s):
    for c in [chr(i) for i in range(ord('*'), ord('b') + 1)]:
        s = s.replace(c, '') if 42 <= s.find(c) <= 97 else s
    return s