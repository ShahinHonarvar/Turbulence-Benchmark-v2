def filter_chars(string):
    return ''.join([char for char in string if char < '>' and char > 'A' or char not in string[33:36]])