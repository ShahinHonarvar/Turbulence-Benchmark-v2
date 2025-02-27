def filter_chars(text):
    return ''.join([ch for ch in text if not (20 <= text.index(ch) <= 62 and 'i' <= ch <= 'k')])