def filter_chars(s):
    chars_to_remove = set()
    for i, char in enumerate(s):
        if 63 <= i <= 84 and 'E' <= char <= '~':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))