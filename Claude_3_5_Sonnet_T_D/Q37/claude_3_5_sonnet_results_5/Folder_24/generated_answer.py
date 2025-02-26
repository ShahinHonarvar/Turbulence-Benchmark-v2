def filter_chars(string):
    chars_to_remove = set((char for i, char in enumerate(string) if 36 <= i <= 79 and '2' <= char <= 's'))
    return ''.join((char for char in string if char not in chars_to_remove))