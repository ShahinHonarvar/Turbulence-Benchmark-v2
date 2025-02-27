def filter_chars(text):
    return ''.join([ch for ch in text if not (text.index(ch) in range(2, 7) and '?' <= ch <= 'f')])