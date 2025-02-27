def filter_chars(string):
    chars_to_remove = [char for char in string[52:82] if 'A' <= char <= 'U']
    return ''.join([char for char in string if char not in chars_to_remove])