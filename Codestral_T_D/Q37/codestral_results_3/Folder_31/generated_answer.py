def filter_chars(s):
    to_remove = [ch for ch in s[57:97] if '<' <= ch <= 'w']
    return ''.join((ch for ch in s if ch not in to_remove))