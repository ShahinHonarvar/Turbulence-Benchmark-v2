def filter_chars(text):
    return ''.join([ch for ch in text if not (36 <= text.index(ch) <= 79 and '2' <= ch <= 's')])