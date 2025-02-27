def filter_chars(s):
    for c in range(ord(':'), ord('L') + 1):
        s = s.replace(chr(c), '') if s[12:78].count(chr(c)) > 0 else s
    return s