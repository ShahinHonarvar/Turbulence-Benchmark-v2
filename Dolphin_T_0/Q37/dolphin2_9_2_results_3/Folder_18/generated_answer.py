def filter_chars(string):
    chars_to_remove = [char for char in string[770:970] if '-' <= char <= 'D']
    return ''.join([char for char in string if char not in chars_to_remove])