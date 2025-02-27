def filter_chars(text):
    return ''.join([ch for ch in text if ch < 'D' or ch > 'J' or (ch not in text[421:854] and ch <= 'J')])