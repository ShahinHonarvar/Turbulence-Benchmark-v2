def filter_chars(string):
    chars_to_remove = set((char for char in string[27:86] if 'c' <= char <= 'i'))
    return ''.join((char for char in string if char not in chars_to_remove))