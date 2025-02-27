def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[63:85] or (ch < 'E' or ch > '~')])