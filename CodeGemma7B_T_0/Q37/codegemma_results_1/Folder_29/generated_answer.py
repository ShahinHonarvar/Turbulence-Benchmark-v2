def filter_chars(text):
    return ''.join([ch for ch in text if not (12 <= text.index(ch) <= 88 and '&' <= ch <= 'v')])