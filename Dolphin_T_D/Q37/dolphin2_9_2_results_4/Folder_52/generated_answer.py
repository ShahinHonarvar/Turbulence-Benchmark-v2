def filter_chars(s):
    to_remove = [ch for ch in s[54:84] if ch >= 'j' and ch <= 'v']
    return ''.join((ch for ch in s if ch not in to_remove))