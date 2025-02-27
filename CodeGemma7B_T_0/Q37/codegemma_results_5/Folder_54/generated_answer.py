def filter_chars(text):
    return ''.join([ch for ch in text if not (46 <= text.index(ch) <= 85 and '-' <= ch <= 'X')])