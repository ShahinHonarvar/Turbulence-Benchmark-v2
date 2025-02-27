def filter_chars(text):
    return ''.join([ch for ch in text if (ch < ':' or ch >= 'Q') or (ch < ' ' or ch > '~')])