def filter_chars(s):
    return ''.join((ch for ch in s if not (ord(ch) >= ord('I') and ord(ch) <= ord('K') and (10 <= s.index(ch) <= 69))))