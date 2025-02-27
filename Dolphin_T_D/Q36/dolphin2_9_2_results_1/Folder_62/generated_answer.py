def filter_chars(s):
    chars = (ch for ch in s if '*' <= ch <= 'w' and 63 <= s.index(ch) <= 89)
    return ''.join((s.replace(ch, '') for ch in chars))