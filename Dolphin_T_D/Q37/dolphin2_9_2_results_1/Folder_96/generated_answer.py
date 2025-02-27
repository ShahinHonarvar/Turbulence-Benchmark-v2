def filter_chars(text):
    return ''.join([ch for i, ch in enumerate(text) if not (86 <= i <= 92 and '!' <= ch <= 's')])