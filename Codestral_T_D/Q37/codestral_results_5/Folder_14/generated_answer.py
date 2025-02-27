def filter_chars(s):
    return ''.join((ch for i, ch in enumerate(s) if not (35 <= i <= 98 and 'A' <= ch <= 'b')))