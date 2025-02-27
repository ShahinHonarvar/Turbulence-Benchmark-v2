def filter_chars(text):
    return ''.join([ch for ch in text if not (41 <= ord(ch) <= 64 and 'K' <= ch <= ']')])