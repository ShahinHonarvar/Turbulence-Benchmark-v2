def filter_chars(text):
    return ''.join([ch for ch in text if not (51 <= ord(ch) <= 96 and 'X' <= ch <= 'p')])