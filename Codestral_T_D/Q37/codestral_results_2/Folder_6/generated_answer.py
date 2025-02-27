def filter_chars(s):
    for c in [chr(i) for i in range(ord('c'), ord('n') + 1)]:
        s = s.replace(c, '') if s[13:29].count(c) > 0 else s
    return s