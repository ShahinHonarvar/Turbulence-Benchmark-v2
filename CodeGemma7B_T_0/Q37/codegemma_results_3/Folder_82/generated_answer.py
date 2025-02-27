def filter_chars(text):
    return ''.join([ch for ch in text if not (ch >= 'P' and ch <= 'x' and (12 <= text.index(ch) <= 25))])