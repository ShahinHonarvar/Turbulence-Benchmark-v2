def filter_chars(text):
    return ''.join([ch for ch in text if not (86 <= text.index(ch) <= 92 and '!' <= ch <= 's')])