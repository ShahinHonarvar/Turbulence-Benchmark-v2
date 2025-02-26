def filter_chars(string):
    chars_to_remove = set((char for i, char in enumerate(string) if 722 <= i <= 832 and 'K' <= char <= 'm'))
    return ''.join((char for char in string if char not in chars_to_remove))