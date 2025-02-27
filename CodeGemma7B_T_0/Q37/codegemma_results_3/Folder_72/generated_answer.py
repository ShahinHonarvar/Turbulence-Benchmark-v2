def filter_chars(text):
    return ''.join([ch for ch in text if not (35 <= text.index(ch) <= 51 and 'H' <= ch <= 's')])