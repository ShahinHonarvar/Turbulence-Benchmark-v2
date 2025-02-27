def filter_chars(text):
    return ''.join([ch for ch in text if not (13 <= text.index(ch) <= 28 and 'c' <= ch <= 'n')])