def filter_chars(text):
    return ''.join([c for i, c in enumerate(text) if i not in range(27, 30) or not (c >= ';' and c <= 'b')])