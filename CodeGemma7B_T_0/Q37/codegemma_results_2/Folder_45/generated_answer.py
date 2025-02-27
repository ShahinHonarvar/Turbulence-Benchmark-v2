def filter_chars(text):
    return ''.join([ch for ch in text if not (72 <= ord(ch) <= 94 and '.' <= ch <= 'b')])