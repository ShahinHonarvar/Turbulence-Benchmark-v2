def filter_chars(s):
    to_remove = set((char for char in s[18:82] if 'W' <= char <= '['))
    return ''.join((char for char in s if char not in to_remove))