def filter_chars(text):
    return ''.join([ch for ch in text if not (33 <= ord(ch) <= 70 and '7' <= ch <= 'k')])