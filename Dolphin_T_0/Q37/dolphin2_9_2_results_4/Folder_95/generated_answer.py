def filter_chars(string):
    chars_to_remove = [char for char in string[35:41] if char >= ')' and char <= 'l']
    return ''.join([char for char in string if char not in chars_to_remove])