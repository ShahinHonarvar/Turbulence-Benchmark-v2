def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[373:902] or (ch < 'T' or ch > 'h')])