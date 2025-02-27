def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[75:100] or (ch < '8' or ch > 'e')])