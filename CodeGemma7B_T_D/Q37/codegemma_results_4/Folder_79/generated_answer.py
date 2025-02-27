def filter_chars(txt):
    return ''.join([ch for ch in txt if not (10 <= txt.index(ch) <= 52 and '@' <= ch <= 'T')])