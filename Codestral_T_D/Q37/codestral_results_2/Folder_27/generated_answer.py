def filter_chars(string):
    for char in string[43:81]:
        if '=' <= char <= 'E':
            string = string.replace(char, '')
    return string