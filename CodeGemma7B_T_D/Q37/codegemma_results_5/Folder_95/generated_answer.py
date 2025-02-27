def filter_chars(s):
    return ''.join([ch for ch in s if not (35 <= s.index(ch) <= 40 and ')' <= ch <= 'l')])