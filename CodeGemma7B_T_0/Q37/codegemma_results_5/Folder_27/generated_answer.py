def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[43:81] or (ch >= '=' and ch <= 'E')])