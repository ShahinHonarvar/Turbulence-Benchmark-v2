def filter_chars(s):
    to_remove = [ch for ch in s[36:41] if 'H' <= ch <= 'e']
    return ''.join([ch for ch in s if ch not in to_remove])