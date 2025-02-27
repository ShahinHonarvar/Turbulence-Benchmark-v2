def filter_chars(text):
    return ''.join([ch for ch in text if not (38 <= text.index(ch) <= 54 and ':' <= ch <= 'r')])