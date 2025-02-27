def filter_chars(txt):
    return ''.join((c for c in txt if c < '3' or c > 'B' or (c > '9' and c < 'A')))