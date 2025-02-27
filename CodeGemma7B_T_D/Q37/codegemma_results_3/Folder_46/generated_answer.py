def filter_chars(text):
    return ''.join([c for c in text if not (i >= 11 and i <= 72 and (c >= 'i') and (c <= 'v'))])