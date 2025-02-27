def filter_chars(text):
    return ''.join([ch for ch in text if not (10 <= text.index(ch) <= 69 and 'I' <= ch <= 'K')])