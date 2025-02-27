def filter_chars(txt):
    chars_to_remove = [char for char in txt[12:26] if 'P' <= char <= 'x']
    return ''.join([char for char in txt if char not in chars_to_remove])