def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[42:93] or (ch < '/' or ch > 'a')])