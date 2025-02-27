def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[23:89] or (ch < 'w' or ch > '{')])