def filter_chars(text):
    return ''.join([ch for ch in text if not (32 <= ord(ch) <= 46 and '0' <= ch <= 'k')])