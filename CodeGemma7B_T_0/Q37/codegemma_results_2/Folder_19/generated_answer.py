def filter_chars(text):
    return ''.join([ch for ch in text if not (35 <= ord(ch) <= 89 and 'E' <= ch <= 't')])