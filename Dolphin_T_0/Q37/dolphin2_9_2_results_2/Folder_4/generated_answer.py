def filter_chars(s):
    to_remove = [ch for i, ch in enumerate(s) if 19 <= i <= 33 and 'S' <= ch <= '{']
    return ''.join([ch for ch in s if ch not in to_remove])