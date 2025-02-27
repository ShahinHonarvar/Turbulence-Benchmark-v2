def filter_chars(txt):
    return ''.join([c for c in txt if ord(c) not in range(42, 57) or not (c > 'Z' and c < 'c')])