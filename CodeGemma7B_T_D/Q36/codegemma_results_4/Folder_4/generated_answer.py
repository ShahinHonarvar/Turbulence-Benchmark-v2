def filter_chars(txt):
    return ''.join((ch for ch in txt if not (ch in range(42, 67) and (ch > '6' and ch < 'g'))))