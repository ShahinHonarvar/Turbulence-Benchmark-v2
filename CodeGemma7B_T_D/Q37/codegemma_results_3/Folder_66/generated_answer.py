def filter_chars(string):
    return ''.join([char for char in string if not (27 <= ord(char) <= 85 and 'c' <= char <= 'i')])