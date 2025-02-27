def filter_chars(text):
    return ''.join([c for c in text if not (56 <= ord(c) <= 86 and '+' < c < 'w')])