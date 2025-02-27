def filter_chars(text):
    return ''.join([ch for ch in text if not (17 <= text.index(ch) <= 63 and 'O' <= ch <= '^')])