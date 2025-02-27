def filter_chars(string):
    for char in set(string[75:100]):
        if '8' <= char <= 'e':
            string = string.replace(char, '')
    return string