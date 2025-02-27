def filter_chars(text):
    return ''.join([ch for ch in text if not (42 <= ord(ch) <= 97 and '*' <= ch <= 'b')])