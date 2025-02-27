def filter_chars(string):
    to_remove = [char for char in string[12:89] if '&' <= char <= 'v']
    return ''.join([char for char in string if char not in to_remove])