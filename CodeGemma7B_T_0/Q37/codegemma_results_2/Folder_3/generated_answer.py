def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[37:57] or (ch < '6' or ch > '_')])