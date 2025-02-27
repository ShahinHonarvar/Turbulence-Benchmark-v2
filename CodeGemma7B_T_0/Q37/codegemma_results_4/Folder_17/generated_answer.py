def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[27:30] or (ch < ';' or ch > 'b')])