def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[3:8] or (ch > '?' and ch < 'k')])