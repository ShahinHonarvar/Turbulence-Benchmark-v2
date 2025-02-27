def filter_chars(text):
    return ''.join([ch for ch in text if not (34 <= text.index(ch) <= 67 and 'W' <= ch <= 'x')])