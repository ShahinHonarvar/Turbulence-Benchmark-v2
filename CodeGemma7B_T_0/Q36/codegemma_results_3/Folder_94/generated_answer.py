def filter_chars(text):
    return ''.join([ch for ch in text if not (ch > 'I' and ch < 'M' and (15 < text.index(ch) < 85))])