def filter_chars(txt):
    return ''.join([ch for ch in txt if 138 <= txt.index(ch) <= 920 and ch >= '6' and (ch <= 'A')])