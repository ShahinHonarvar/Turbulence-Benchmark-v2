def filter_chars(text):
    return ''.join([ch for ch in text if not (41 <= text.index(ch) <= 86 and 'S' <= ch <= 's')])