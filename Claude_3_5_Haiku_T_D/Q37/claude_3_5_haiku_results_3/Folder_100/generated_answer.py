def filter_chars(s):
    chars_to_remove = set((char for i, char in enumerate(s) if 88 <= i <= 90 and 'J' <= char <= 'Q'))
    return ''.join((char for char in s if char not in chars_to_remove))