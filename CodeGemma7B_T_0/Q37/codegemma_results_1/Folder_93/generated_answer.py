def filter_chars(text):
    return ''.join([ch for ch in text if not (38 <= text.index(ch) <= 69 and 'H' <= ch <= 'e')])