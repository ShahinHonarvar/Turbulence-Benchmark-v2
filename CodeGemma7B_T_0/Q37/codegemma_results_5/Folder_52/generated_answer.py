def filter_chars(text):
    return ''.join([ch for ch in text if not (54 <= ord(ch) <= 83 and 'j' <= ch <= 'v')])