def filter_chars(input_string):
    return ''.join([char for char in input_string if not (513 <= input_string.index(char) <= 877 and '?' <= char <= 'n')])