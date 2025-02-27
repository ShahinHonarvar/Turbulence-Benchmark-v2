def filter_chars(string):
    return ''.join([char for char in string if char not in string[55:84] or not (char > ';' and char < 'z')])