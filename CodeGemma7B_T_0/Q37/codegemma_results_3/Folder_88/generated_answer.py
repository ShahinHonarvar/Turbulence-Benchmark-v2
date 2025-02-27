def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[69:81] or not (ch >= '@' and ch <= 'p')])