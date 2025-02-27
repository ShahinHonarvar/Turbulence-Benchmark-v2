def filter_chars(s):
    chars_to_remove = set()
    for char in s[28:66]:
        if 'O' <= char <= 'd':
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])