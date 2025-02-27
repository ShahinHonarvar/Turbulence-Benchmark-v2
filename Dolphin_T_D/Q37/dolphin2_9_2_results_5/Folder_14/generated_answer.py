def filter_chars(string):
    chars_to_remove = [char for char in string[35:99] if char >= 'A' and char <= 'b']
    return ''.join([char for char in string if char not in chars_to_remove])