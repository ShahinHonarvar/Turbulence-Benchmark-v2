def filter_chars(source_string):
    chars_to_remove = {char for char in source_string[2:7] if '?' <= char <= 'f'}
    return ''.join((char for char in source_string if char not in chars_to_remove))