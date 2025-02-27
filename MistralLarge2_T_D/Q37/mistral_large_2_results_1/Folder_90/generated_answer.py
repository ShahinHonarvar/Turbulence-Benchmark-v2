def filter_chars(s):
    chars_to_remove = set((char for i, char in enumerate(s) if 348 <= i <= 852 and 'J' <= char <= 'b'))
    return ''.join((char for char in s if char not in chars_to_remove))