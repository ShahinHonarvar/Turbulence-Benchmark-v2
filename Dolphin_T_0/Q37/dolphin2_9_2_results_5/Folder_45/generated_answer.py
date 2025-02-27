def filter_chars(string):
    chars_to_remove = [string[i] for i in range(72, 95) if string[i] >= '.' and string[i] <= 'b']
    return ''.join([char for char in string if char not in chars_to_remove])