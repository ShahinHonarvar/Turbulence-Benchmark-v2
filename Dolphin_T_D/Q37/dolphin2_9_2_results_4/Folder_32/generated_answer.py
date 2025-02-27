def filter_chars(s):
    return ''.join((ch for ch in s if 23 <= s.index(ch) <= 89 and 'w' <= ch < '{'))