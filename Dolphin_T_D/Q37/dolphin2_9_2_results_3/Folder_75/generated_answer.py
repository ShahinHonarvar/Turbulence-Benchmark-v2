def filter_chars(string):
    result = [char for char in string if 34 <= string.index(char) <= 67 and 'W' <= char <= 'x']
    new_string = ''.join([char for char in string if char not in result])
    return new_string