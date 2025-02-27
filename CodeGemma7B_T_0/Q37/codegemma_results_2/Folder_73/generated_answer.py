def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[22:86] or (ch < '7' or ch > 'e')])