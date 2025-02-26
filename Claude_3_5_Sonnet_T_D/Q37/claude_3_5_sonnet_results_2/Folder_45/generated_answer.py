def filter_chars(string):
    chars_to_remove = set((char for i, char in enumerate(string) if 72 <= i <= 94 and '.' <= char <= 'b'))
    return ''.join((char for char in string if char not in chars_to_remove))