def filter_chars(s):
    remove_chars = set((char for char in s[7:9] if 'B' <= char <= 'H'))
    return ''.join((char for char in s if char not in remove_chars))