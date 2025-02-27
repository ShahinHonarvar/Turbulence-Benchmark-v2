def filter_chars(s):
    to_remove = {char for char in s[225:382] if 'D' <= char <= 'Y'}
    return ''.join((char for char in s if char not in to_remove))