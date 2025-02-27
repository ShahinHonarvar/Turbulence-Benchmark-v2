def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[513:878] or (ch < '?' or ch > 'n')])