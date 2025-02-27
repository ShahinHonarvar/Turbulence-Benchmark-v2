def filter_chars(string):
    for char in sorted(set(string[72:95])):
        if '.' <= char <= 'b':
            string = string.replace(char, '')
    return string