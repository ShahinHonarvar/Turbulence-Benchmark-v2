def filter_chars(s):
    to_remove = [ch for ch in s[13:29] if 'c' <= ch <= 'n']
    return ''.join((ch for ch in s if ch not in to_remove))