def filter_chars(string):
    result = [char for char in string if not (27 <= string.index(char) <= 29 and ';' <= char <= 'b')]
    return ''.join(result)