def filter_chars(s):
    chars_to_remove = set((char for char in s[23:90] if 'w' <= char <= '{'))
    return ''.join((char for char in s if char not in chars_to_remove))