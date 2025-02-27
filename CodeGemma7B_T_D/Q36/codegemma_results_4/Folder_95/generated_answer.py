def filter_chars(str):
    return ''.join([c for c in str if not (56 < ord(c) < 86 and '+' < c < 'w')])