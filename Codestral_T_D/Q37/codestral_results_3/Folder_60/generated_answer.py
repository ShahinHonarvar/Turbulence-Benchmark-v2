def filter_chars(string):
    for char in string[12:78]:
        if ':' <= char <= 'L':
            string = string.replace(char, '')
    return string